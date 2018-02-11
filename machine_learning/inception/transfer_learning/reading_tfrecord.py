import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import os


# User guide:
# Specify tfrecord path from where you want to extract images.
# Specify output directory where to save extracted images.

# Tfrecord path
tfrecord_filename = '../../../../../Documents/CarAppML/cars/cars_validation_00000-of-00002.tfrecord'

# Val data directory path
val_dir_path = '../../../../../Documents/CarAppML/cars/val_data/audi/'


if __name__ == "__main__":
    record_iterator = tf.python_io.tf_record_iterator(path=tfrecord_filename)
    print(record_iterator)
    images = {}
    sess = tf.Session()
    i = 1
    for string_record in record_iterator:
        example = tf.train.Example()
        example.ParseFromString(string_record)
        height = int(example.features.feature['image/height'].int64_list.value[0])
        width = int(example.features.feature['image/width'].int64_list.value[0])
        img_string = example.features.feature['image/encoded'].bytes_list.value[0]
        img_decoded = tf.image.decode_jpeg(img_string, channels=3)
        img = sess.run(img_decoded)
        im = Image.fromarray(img)
        im.save(os.path.join(val_dir_path, 'val_image_'+str(i)+'.jpg'))
        i += 1

