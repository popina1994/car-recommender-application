import tensorflow as tf
from transfer_learning.inception_resnet_v2 import inception_resnet_v2, inception_resnet_v2_arg_scope
from transfer_learning.inception_preprocessing import preprocess_image
from PIL import Image
import numpy as np
import os
import time
slim = tf.contrib.slim

"""
Instructions:
This script contains definiton of a class ConvNetModel which is used for
restoring pretrained checkpoint model. Before starting it is necessary to
obtain all the necessary files and set up the environment.
Please, follow next steps.

1. You can find checkpoint files under LOG directory on this link
https://mega.nz/#F!vdpmRahT!8XL_MyllciU162Z-udIL5w!iAAQkTQI.
Download this directory to your local machine.

2. Check if LOG directory contains labels.txt file. If not present there,
you have to find its true location. In this file are listed
labels for each car model.

3. Secure that you have installed following packages: tensorflow, numpy, PIL.

After finishing these steps, everything should be ready.
Here is an example of using ConvNetModel class.

    ################################################################
    # Loading checkpoint model. This command is called only once and
      the model is loaded into memory.
    model = ConvNetModel(checkpoint_dir=log_dir)

    # Predict car model. This command is used whenever you want to
      do prediction.
    pred = model.predict(image_path='./val_data/bmw/val_image_1.jpg')
    #################################################################

"""

num_classes = 13

#Log directory where checkpoint model is saved
log_dir = '../../../bmw_log/log'

#Labels path
labels_path = './log/labels.txt'


class ConvNetModel(object):
    def __init__(self, checkpoint_dir, labels_path=None, num_classes=num_classes):
        """
        Checkpoint model is loaded during initialization.
        :param checkpoint_dir: Directory where checkpoint model is saved
        :param labels_path: Labels path. If this is None then it is contained in checkpoint_dir.
        :param num_classes: Number of classes
        """
        # Get the latest checkpoint file from checkpoint directory
        self.checkpoint_file = tf.train.latest_checkpoint(checkpoint_dir)
        self.num_classes = num_classes
        self.height = 299
        self.width = 299

        # Read labels
        if labels_path is None:
            labels_path = os.path.join(checkpoint_dir, 'labels.txt')
        self.labels = {}
        with open(labels_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line[:-1].split(":")
                label = int(line[0])
                label_name = line[1]
                self.labels[label] = label_name

        # Reset all graphs before
        tf.reset_default_graph()

        # Set CPU for running
        config = tf.ConfigProto(
           device_count={'GPU': 0}
        )
        self.sess = tf.Session(config=config)

        self.image_placeholder = tf.placeholder(dtype=tf.uint8,
                                                shape=(None, None, 3),
                                                name="input_image")
        image_processed = preprocess_image(self.image_placeholder,
                                           self.height,
                                           self.width,
                                           is_training=False)
        image_input = tf.expand_dims(image_processed, 0)

        with slim.arg_scope(inception_resnet_v2_arg_scope()):
            logits, end_points = inception_resnet_v2(image_input,
                                                     num_classes=self.num_classes,
                                                     is_training=False)
        self.logits = logits
        self.predictions = tf.argmax(end_points['Predictions'], 1)

        # Restore model from checkpoint file
        saver = tf.train.Saver()
        saver.restore(self.sess, self.checkpoint_file)

    def predict(self, image_path):
        """
        Predicts class(label) of the loaded image.
        :param image_path: Image path
        :return: Label's number
        """
        img = Image.open(image_path)
        img = np.asarray(img)
        logits_eval, pred = self.sess.run([self.logits, self.predictions],
                                          feed_dict={self.image_placeholder: img})
        return pred[0], self.labels[pred[0]]


if __name__ == "__main__":
    import glob
    import cv2
    import random
    from create_tfrecords.dataset_utils import _get_filenames_and_classes
    #filenames = glob.glob("../../../bmw/cars_for_testing/*.jpg")
    #filenames = sorted(filenames, key=lambda f: int(os.path.basename(f).split("_")[0]))
    photo_filenames, class_names = _get_filenames_and_classes("../../../bmw/bmw_dataset")
    class_names_to_ids = dict(zip(class_names, range(len(class_names))))
    # Find the number of validation examples we need
    num_validation = int(0.1 * len(photo_filenames))

    # Divide the training datasets into train and test:
    random.seed(0)
    random.shuffle(photo_filenames)
    validation_filenames = photo_filenames[:num_validation]

    labels = []
    pred_labels = []
    model = ConvNetModel(checkpoint_dir=log_dir, labels_path=None)
    for i, filename in enumerate(validation_filenames):
        if i % 50 == 0:
            print(i)
        class_name = os.path.basename(os.path.dirname(filename))
        class_id = class_names_to_ids[class_name]
        labels.append(int(class_id))
        pred_label, _ = model.predict(filename)
        pred_labels.append(pred_label)

    labels = np.array(labels)
    print(labels)
    pred_labels = np.array(pred_labels)
    acc = np.sum(labels == pred_labels) / len(labels)
    print(acc)



    #model = ConvNetModel(checkpoint_dir=log_dir, labels_path=None)
    #for i, file_path in enumerate(filenames):
    #    pred, label = model.predict(image_path=filenames[i])
    #    image_name = os.path.basename(file_path).split("_")
    #    print(image_name[0], " ", image_name[1]+image_name[2], " ", label)






    # Loading checkpoint model
    #model = ConvNetModel(checkpoint_dir=log_dir, labels_path=labels_path)

    # Predict car model
    #pred = model.predict(image_path='../../../../CarAppML/cars/val_data/bmw/val_image_1.jpg')

    #pred = model.predict(image_path='../../../../CarAppML/bmw_test_for_check.jpg')
    #print(pred)
