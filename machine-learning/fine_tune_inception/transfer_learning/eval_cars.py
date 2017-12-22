import tensorflow as tf
from tensorflow.python.platform import tf_logging as logging
from tensorflow.contrib.framework.python.ops.variables import get_or_create_global_step
import  transfer_learning.inception_preprocessing
from transfer_learning.inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope
import time
import os
from transfer_learning.train_cars import get_split, load_batch
import matplotlib.pyplot as plt
plt.style.use('ggplot')
slim = tf.contrib.slim


#State the log directory frow where to retrieve the model
log_dir = './log'

#Create a new evaluation log directory to visualize the validation process
log_eval = './log_eval_test'

#State the directory where the validation set is found
dataset_dir = '../flowers/'

#State the batch size used for evaluation
batch_size = 36

#State the number of epochs to evaluate
num_epochs = 3

#Get the latest checkpoint file
checkpoint_file = tf.train.latest_checkpoint(log_dir)


def run():
  #Create log dir
  if not os.path.exists(log_eval):
    os.mkdir(log_eval)

  #Just construct the graph from scratch again
  with tf.Graph().as_default() as graph:
    tf.logging.set_verbosity(tf.logging.INFO)
    dataset = get_split('validation', dataset_dir)
    images, raw_images, labels = load_batch(dataset, batch_size=batch_size, is_training=False)

    #Info about training steps
    num_batches_per_epoch = int(dataset.num_samples / batch_size)
    num_steps_per_epoch = num_batches_per_epoch

    #Create inference model with is_training=False
    with slim.arg_scope(inception_resnet_v2_arg_scope()):
      logits, end_points = inception_resnet_v2(images, num_classes=dataset.num_classes, is_training=False)

    #Restore variables from checkpoint
    variables_to_restore = slim.get_variables_to_restore()
    saver = tf.train.Saver(variables_to_restore)
    def restore_fn(sess):
      return saver.restore(sess, checkpoint_file)

    #Define the metrics to track
    predictions = tf.argmax(end_points['Predictions'], 1)
    accuracy, accuracy_update = tf.contrib.metrics.streaming_accuracy(predictions, labels)
    metrics_op = tf.group(accuracy_update)

    #Create global step
    global_step = get_or_create_global_step()
    global_step_op = tf.assign(global_step, global_step + 1)

    #Create a evaluation step function
    def eval_step(sess, metrics_op, global_step):
      start_time = time.time()
      _, global_step_count, accuracy_value = sess.run([metrics_op, global_step_op, accuracy])
      time_elapsed = time.time() - start_time

      #Log some information
      logging.info('Global step %s: Streaming accuracy: %.4f, (%.2f sec/step)', global_step_count, accuracy_value, time_elapsed)

      return accuracy_value

    #Define some scalar quantities to monitor
    tf.summary.scalar('Validation accuracy', accuracy)
    my_summary_op = tf.summary.merge_all()

    #Get your supervisor
    sv = tf.train.Supervisor(logdir = log_eval, summary_op=None, saver=None, init_fn=restore_fn)

    #Start evaluation
    with sv.managed_session() as sess:
      for step in range(num_steps_per_epoch * num_epochs):
        sess.run(sv.global_step)

        if step % num_batches_per_epoch == 0:
          logging.info('Epoch: %s/%s', step / num_batches_per_epoch + 1, num_epochs)
          logging.info('Current streaming accuracy: %.4f', sess.run(accuracy))

        if step % 10 == 0:
          eval_step(sess, metrics_op = metrics_op, global_step=sv.global_step)
          summaries = sess.run(my_summary_op)
          sv.summary_computed(sess, summaries)
        else:
          eval_step(sess, metrics_op = metrics_op, global_step = sv.global_step)
      logging.info('Final streamming accuarcy: %.4f', sess.run(accuracy))

      logging.info('Model evaluation has completed! Visit TensorBoard for more information regarding your evaluation.')


if __name__ == '__main__':
  run()






