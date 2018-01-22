import random
import tensorflow as tf
import os
from create_tfrecords.dataset_utils import _dataset_exists, _get_filenames_and_classes, write_label_file, _convert_dataset

flags = tf.app.flags

# State your dataset directory
flags.DEFINE_string('dataset_dir', None, 'String: Your original dataset directory')

# Proportion of dataset to be used for evaluation
flags.DEFINE_float('validation_size', 0.3, 'Float: The proportion of examples in the dataset to be used for validation')

# The number of shards to split the dataset into
flags.DEFINE_integer('num_shards', 2, 'Int: Number of shards to split the TFRecord files into')

# Seed for repeatibility
flags.DEFINE_integer('random_seed', 0, 'Int: Random seed to use for repeatibility')

# Output filename for naming the TFRecord file
flags.DEFINE_string('tfrecord_filename', None, 'String: The output filename to name TFrecord file')

FLAGS = flags.FLAGS

if __name__ == "__main__":
  # ==============================================================CHECKS==========================================================================
  # Check if there is a tfrecord_filename entered
  if not FLAGS.tfrecord_filename:
    raise ValueError('tfrecord_filename is empty. Please state a tfrecord_filename argument.')

  # Check if there is a dataset directory entered
  if not FLAGS.dataset_dir:
    raise ValueError('dataset_dir is empty. Please state a dataset_dir argument.')

  # If the TFRecord files already exist in the directory, then exit without creating the files again
  if _dataset_exists(dataset_dir=FLAGS.dataset_dir, _NUM_SHARDS=FLAGS.num_shards,
                     output_filename=FLAGS.tfrecord_filename):
    print('Dataset files already exist. Exiting without re-creating them.')
    exit()
  # ==============================================================END OF CHECKS===================================================================


  photo_filenames, class_names = _get_filenames_and_classes(FLAGS.dataset_dir)
  class_names_to_ids = dict(zip(class_names, range(len(class_names))))

  # Obtain num of validation examples
  num_validation =  int(FLAGS.validation_size * len(photo_filenames))

  # Divide data to train and val
  random.seed(FLAGS.random_seed)
  random.shuffle(photo_filenames)
  training_filenames = photo_filenames[num_validation:]
  validation_filenames = photo_filenames[:num_validation]

  # Convert the training and val sets.
  _convert_dataset('train', training_filenames, class_names_to_ids,
                   dataset_dir=FLAGS.dataset_dir,
                   tfrecord_filename=FLAGS.tfrecord_filename,
                   _NUM_SHARDS=FLAGS.num_shards)

  _convert_dataset('validation', validation_filenames, class_names_to_ids,
                   dataset_dir=FLAGS.dataset_dir,
                   tfrecord_filename=FLAGS.tfrecord_filename,
                   _NUM_SHARDS=FLAGS.num_shards)

  # Write labels file
  labels_to_class_names = dict(zip(range(len(class_names)), class_names))
  write_label_file(labels_to_class_names, FLAGS.dataset_dir)

  print ("Finished converting images to TFRecords")