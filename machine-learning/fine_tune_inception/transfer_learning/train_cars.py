import tensorflow as tf
from tensorflow.contrib.framework.python.ops.variables import get_or_create_global_step
from tensorflow.python.platform import tf_logging as logging
import transfer_learning.inception_preprocessing
from transfer_learning.inception_preprocessing import  preprocess_image
from transfer_learning.inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope
import os
import time

slim = tf.contrib.slim

#=================== DATASET INFORMATION =====================
#State dataset directory where  the tfrecords files are located
dataset_dir = '../flowers/'

#State where your log file is at. If it doesn't exist, create it.
log_dir = './log'

#State where your checkpoint file is
checkpoint_file = './inception_resnet_v2_2016_08_30.ckpt'

#State the number of classes to predict
num_classes = 5

#State the image size
image_size = 299

#State the labels file and read it
labels_file = '../flowers/labels.txt'
labels = open(labels_file, 'r')

#Create a dictionary to refer each label to its string name
labels_to_name = {}
for line in labels:
  label, string_name = line.split(':')
  string_name = string_name[:-1]
  labels_to_name[int(label)] = string_name

#Create the file pattern of TFRecords so that it could be recognized later
file_pattern = 'flowers_%s_*.tfrecord'

#Name of the objects
name_of_objects = 'flowers'

#Create a dictionary that will explain dataset more deeply. This is required by the Dataset class later.
items_to_description = {
  'image': 'A 3-channel RGB coloured flower image that is either tulips, sunflowers, roses, dandelion or daisy',
  'label': 'A label that is as such -- 0:daisy, 1:dandelion, 2:roses, 3:sunflowers, 4:tulips'
}

#=================== TRAINING INFORMATION =============================
#State the number of epochs to train
num_epochs = 1

#State the batch size
batch_size = 10

#Learning rate information and configuration
initial_learning_rate = 0.0002
learning_rate_decay_factor = 0.7
num_epochs_before_decay = 2

def get_split(split_name, dataset_dir, file_pattern=file_pattern):
  """
  Obtains the split - training or validation - to create a Dataset class for feeding the examples into a queue later
  on. This function will set up the decoder and dataset information all into one Dataset class so that you can avoid
  the brute work later on.

  Your file_pattern is very important in locating the files later.

  INPUTS:
      - split_name(str): 'train' or 'validation'. Used to get the correct data split of tfrecord files
      - dataset_dir(str): the dataset directory where the tfrecord files are located
      - file_pattern(str): the file name structure of the tfrecord files in order to get the correct data

  OUTPUTS:
  - dataset (Dataset): A Dataset class object where we can read its various components for easier batch creation.
  """

  if split_name not in ['train', 'validation']:
    raise ValueError("The split name %s is not recognized."
                     "Please input either train or validation as split name." % split_name)

  #Create a general file pattern path to locate the tfrecord_files
  file_pattern_path = os.path.join(dataset_dir, file_pattern %(split_name))

  #Count the total num of examples in all of these shards
  num_samples = 0
  file_pattern_for_counting = name_of_objects + '_' + split_name
  tfrecords_to_count = [os.path.join(dataset_dir, file) for file in os.listdir(dataset_dir) if
                        file.startswith(file_pattern_for_counting)]
  for tfrecord_file in tfrecords_to_count:
    for record in tf.python_io.tf_record_iterator(tfrecord_file):
      num_samples += 1
  #Create a reader (TFReader in this case)
  reader = tf.TFRecordReader

  #Create the keys_to_features dictionary for the decoder
  keys_to_features = {
    'image/encoded': tf.FixedLenFeature((), tf.string, default_value=''),
    'image/format': tf.FixedLenFeature((), tf.string, default_value='jpg'),
    'image/class/label': tf.FixedLenFeature([], tf.int64, default_value=tf.zeros([], dtype=tf.int64))
  }

  #Create the items_to_handlers dictionary for the decoder
  items_to_handlers = {
    'image': slim.tfexample_decoder.Image(),
    'label': slim.tfexample_decoder.Tensor('image/class/label')
  }

  #Start to create the decoder
  decoder = slim.tfexample_decoder.TFExampleDecoder(keys_to_features, items_to_handlers)

  #Create the labels_to_name file
  labels_to_name_dict = labels_to_name

  #Actually create the dataset
  dataset = slim.dataset.Dataset(
    data_sources = file_pattern_path,
    decoder = decoder,
    reader = reader,
    num_readers = 4,
    num_samples = num_samples,
    num_classes = num_classes,
    labels_to_name = labels_to_name_dict,
    items_to_descriptions = items_to_description
  )
  return dataset


def load_batch(dataset, batch_size, height=image_size, width=image_size, is_training=True):
  '''
  Loads a batch for training.
  INPUTS:
  - dataset(Dataset): a Dataset class object that is created from the get_split function
  - batch_size(int): determines how big of a batch to train
  - height(int): the height of the image to resize to during preprocessing
  - width(int): the width of the image to resize to during preprocessing
  - is_training(bool): to determine whether to perform a training or evaluation preprocessing
  OUTPUTS:
  - images(Tensor): a Tensor of the shape (batch_size, height, width, channels) that contain one batch of images
  - labels(Tensor): the batch's labels with the shape (batch_size,) (requires one_hot_encoding).
  '''
  # Create DatasetDataProvider class object
  data_provider = slim.dataset_data_provider.DatasetDataProvider(
    dataset,
    common_queue_capacity = 24 + 3 * batch_size,
    common_queue_min = 24
  )

  # Get the raw image
  raw_image, label =  data_provider.get(['image', 'label'])

  #Perform the correct preprocessing for this image depending if it is training or evaluation
  image = preprocess_image(raw_image, height, width, is_training)

  # For raw images, do resizing
  raw_image = tf.expand_dims(raw_image, 0)
  raw_image = tf.image.resize_nearest_neighbor(raw_image, [height, width])
  raw_image = tf.squeeze(raw_image)

  # Batch up the image by enqueueing the tensors internally in a FIFO queue and dequeueing many elements with tf.train.batch
  images, raw_images, labels = tf.train.batch(
    [image, raw_image, label],
    batch_size = batch_size,
    num_threads = 4,
    capacity = 4*batch_size,
    allow_smaller_final_batch = True
  )
  return images, raw_images, labels


def run():
  #Create the log directory here.
  if not os.path.exists(log_dir):
    os.mkdir(log_dir)

  with tf.Graph().as_default() as graph:
    tf.logging.set_verbosity(tf.logging.INFO) #Set verbosity to INFO level

    #Create the dataset and load one batch
    dataset = get_split('train', dataset_dir=dataset_dir, file_pattern=file_pattern)
    images, _, labels = load_batch(dataset, batch_size=batch_size)

    #Set number of steps needed before decaying the learning rate and batches per epoch
    num_batches_per_epoch = dataset.num_samples / batch_size
    num_steps_per_epoch = int(num_batches_per_epoch)
    decay_steps = int(num_epochs_before_decay * num_steps_per_epoch)

    #Create the model inference
    with slim.arg_scope(inception_resnet_v2_arg_scope()):
      logits, end_points = inception_resnet_v2(images, num_classes=dataset.num_classes, is_training=True)

    #Define the scopes to be excluded from the model
    exclude = ['InceptionResnetV2/Logits', 'InceptionResnetV2/AuxLogits']
    variables_to_restore = slim.get_variables_to_restore(exclude=exclude)

    #One-hot encoding of the labels
    one_hot_labels = slim.one_hot_encoding(labels, dataset.num_classes)

    #Loss
    loss = tf.losses.softmax_cross_entropy(onehot_labels=one_hot_labels, logits=logits) #this function adds loss to overall loss
    total_loss = tf.losses.get_total_loss()   #obtain the regularization loss as well

    #Create the global step for monitoring the learning rate and training
    global_step = get_or_create_global_step()

    #Define exponentially decaying learning rate
    lr = tf.train.exponential_decay(
      learning_rate = initial_learning_rate,
      global_step = global_step,
      decay_steps = decay_steps,
      decay_rate = learning_rate_decay_factor,
      staircase = True
    )

    #Define the optimizer that takes on the learning rate
    optimizer = tf.train.AdamOptimizer(learning_rate=lr)

    #Create the train_op
    train_op = slim.learning.create_train_op(total_loss, optimizer)

    #Metrics for prediction
    predictions = tf.argmax(end_points['Predictions'], 1)
    probabilities = end_points['Predictions']
    accuracy, accuracy_update = tf.contrib.metrics.streaming_accuracy(predictions, labels)
    metrics_op = tf.group(accuracy_update)

    #All the summaries we want to track
    tf.summary.scalar('losses/Total_loss', total_loss)
    tf.summary.scalar('accuracy', accuracy)
    tf.summary.scalar('learning_rate', lr)
    my_summary_op = tf.summary.merge_all()

    def train_step(sess, train_op, global_step):
      '''
      Runs the session for the three argument provided and gives a logging on the time elapsed
      '''
      #Check the time for each sess run
      start_time = time.time()
      total_loss, global_step_count, _ =  sess.run([train_op, global_step, metrics_op])
      time_elapsed = time.time() - start_time

      #Run the logging to print some results
      logging.info('global step %s: loss: %.4f (%.2f sec/step)', global_step_count, total_loss, time_elapsed)

      return total_loss, global_step_count

    #Create a saver function that actually restores the variables from a checkpoint file in a sess
    saver = tf.train.Saver(variables_to_restore)
    def restore_fn(sess):
      return saver.restore(sess, checkpoint_file)

    #Define supervisor for running a managed session.
    sv = tf.train.Supervisor(logdir = log_dir, summary_op=None, init_fn = restore_fn)

    #Run the managed session
    with sv.managed_session() as sess:
      for step in range(num_steps_per_epoch * num_epochs):
        print(step)
        #At the start of eevry epoch, show relevant information.
        if step % num_batches_per_epoch == 0:
          logging.info('Epoch %s/%s', step/num_batches_per_epoch + 1, num_epochs)
          learning_rate_value, accuracy_value = sess.run([lr, accuracy])
          logging.info('Current learning rate: %s', learning_rate_value)
          logging.info('Current streaming accuracy: %s', accuracy_value)

        if step % 1000 == 0:
          loss, _ = train_step(sess, train_op, sv.global_step)
          summaries = sess.run(my_summary_op)
          sv.summary_computed(sess, summaries)
        else:
          loss, _ = train_step(sess, train_op, sv.global_step)

      #We log the final training loss and accuracy
      logging.info('Final loss: %s', loss)
      logging.info('Final accuracy: %s', sess.run(accuracy))

      #Once all the training has been done, save the log files and checkpoint model
      logging.info('Finished training! Saving model to disk now.')
      sv.saver.save(sess, sv.save_path, global_step = sv.global_step)


if __name__ == '__main__':
  run()





























