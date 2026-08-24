"""Transfer learning with a pre-trained ResNet50 model in Keras.

This program mirrors the ``TransferLearning.ipynb`` notebook. Using
pre-trained models in Keras is really easy: the ResNet50 model is loaded
with weights already learned from the ImageNet data set, so we can use it
to classify new images into one of 1,000 possible categories without any
training of our own.

Flow
----
1. Load a pre-trained ResNet50 model (``weights='imagenet'``).
2. For each image path:
   a. Load the image and rescale it to the 224x224 resolution the model
      expects,
   b. Convert it to a numpy array and add a batch dimension,
   c. Run it through the model's ``preprocess_input`` to normalize it,
   d. Call ``model.predict`` and decode the top-3 predictions.
3. Print the (class, description, probability) tuples for each image.

Run it with::

    python src/transfer_learning.py --image path/to/image.jpg

You can also pass multiple images. The first time you run it, Keras will
download the pre-trained weights (around 100 MB).

Challenge: try other pre-trained models (e.g. Inception, MobileNet). Bear
in mind different models require different input image sizes.
"""

import argparse

import numpy as np
from tensorflow.keras.applications.resnet50 import (ResNet50, decode_predictions,
                                                    preprocess_input)
from tensorflow.keras.preprocessing import image

# ResNet50 expects 224x224 input images.
IMG_SIZE = (224, 224)
NUM_PREDICTIONS = 3  # number of top predictions to show per image


def load_model():
    """Load ResNet50 with weights pre-trained on the ImageNet data set.

    Returns
    -------
    tensorflow.keras.Model
        The pre-trained classification model.
    """
    return ResNet50(weights='imagenet')


def classify(model, img_path):
    """Classify a single image and print the top predictions.

    Parameters
    ----------
    model : tensorflow.keras.Model
        The pre-trained ResNet50 model.
    img_path : str
        Path to the image file to classify.
    """
    # Load the image and rescale it to the required resolution.
    img = image.load_img(img_path, target_size=IMG_SIZE)

    # Convert to a numpy array, add a batch dimension, and normalize.
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Predict and decode the results into (class, description, probability)
    # tuples (one such list for each sample in the batch).
    preds = model.predict(x)
    print('%s -> Predicted:' % img_path,
          decode_predictions(preds, top=NUM_PREDICTIONS)[0])


def main():
    """Parse command-line arguments and classify each supplied image."""
    parser = argparse.ArgumentParser(
        description='Classify images with a pre-trained ResNet50 model.')
    parser.add_argument('--image', action='append', required=True,
                        dest='images', help='Path to an image to classify. '
                                            'Repeatable: --image a.jpg --image b.jpg')
    args = parser.parse_args()

    model = load_model()

    for img_path in args.images:
        classify(model, img_path)


if __name__ == '__main__':
    main()