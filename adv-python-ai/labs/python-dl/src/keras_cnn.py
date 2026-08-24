"""A Convolutional Neural Network (CNN) on the MNIST data set using Keras.

This program mirrors the ``Keras-CNN.ipynb`` notebook. It improves on the
plain MLP approach by using convolutional layers, which are better suited
for image processing because they are less sensitive to *where* a pattern
appears in the image. With a multi-layer perceptron we achieved around 97%
accuracy; a CNN typically reaches over 99% with just 10 epochs.

Flow
----
1. Load the MNIST data set.
2. Reshape each image into a 28x28x1 tensor (1 grayscale channel) so it can
   be consumed by 2-D convolutional layers. The exact axis order depends on
   whether Keras is configured for ``channels_first`` or ``channels_last``.
3. Normalize pixel values and one-hot encode the labels.
4. Build a CNN: Conv2D(32) -> Conv2D(64) -> MaxPooling2D -> Dropout ->
   Flatten -> Dense(128) -> Dropout -> Dense(10, softmax).
5. Compile with categorical cross-entropy and the Adam optimizer.
6. Train for 10 epochs with a batch size of 32.
7. Evaluate the final model on the test set.

Run it with::

    python src/keras_cnn.py

Warning: training on a CPU can take a very long time (each epoch may take
around 20 minutes) and will max out your CPU. Consider lowering ``EPOCHS``
or using a GPU-accelerated TensorFlow build.
"""

import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras import backend as K
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop

# Hyper-parameters
NUM_CLASSES = 10
BATCH_SIZE = 32
EPOCHS = 10


def load_data():
    """Load and normalize the MNIST data set for convolutional input.

    Each 28x28 image is reshaped into a 28x28x1 tensor (or 1x28x28 if
    Keras uses the ``channels_first`` convention), normalized to [0, 1],
    and the labels are one-hot encoded.

    Returns
    -------
    (train_images, train_labels, test_images, test_labels) : tuple
        The reshaped, normalized image tensors and their one-hot labels.
    """
    (mnist_train_images, mnist_train_labels), \
        (mnist_test_images, mnist_test_labels) = mnist.load_data()

    # Reshape to add the single color channel in the position Keras expects.
    if K.image_data_format() == 'channels_first':
        train_images = mnist_train_images.reshape(
            mnist_train_images.shape[0], 1, 28, 28)
        test_images = mnist_test_images.reshape(
            mnist_test_images.shape[0], 1, 28, 28)
        input_shape = (1, 28, 28)
    else:
        train_images = mnist_train_images.reshape(
            mnist_train_images.shape[0], 28, 28, 1)
        test_images = mnist_test_images.reshape(
            mnist_test_images.shape[0], 28, 28, 1)
        input_shape = (28, 28, 1)

    # Normalize pixel values from [0, 255] to [0, 1].
    train_images = train_images.astype('float32') / 255
    test_images = test_images.astype('float32') / 255

    # One-hot encode the labels.
    train_labels = tensorflow.keras.utils.to_categorical(
        mnist_train_labels, NUM_CLASSES)
    test_labels = tensorflow.keras.utils.to_categorical(
        mnist_test_labels, NUM_CLASSES)

    return train_images, train_labels, test_images, test_labels, input_shape


def display_sample(num, train_images, train_labels):
    """Render a single training sample so we can sanity-check the data.

    Parameters
    ----------
    num : int
        Index of the training sample to display.
    train_images : numpy.ndarray
        The reshaped (28x28x1) training images.
    train_labels : numpy.ndarray
        The one-hot encoded training labels.
    """
    print(train_labels[num])
    label = train_labels[num].argmax(axis=0)
    image = train_images[num].reshape([28, 28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()


def build_model(input_shape):
    """Construct the Keras ``Sequential`` CNN model.

    The topology follows Keras's own MNIST CNN example:
      - 32 3x3 convolution filters on the input image,
      - 64 more 3x3 convolution filters on top of that,
      - 2x2 max-pooling to distill the results,
      - dropout to prevent overfitting,
      - flatten into a 1-D layer,
      - a hidden flat layer of 128 ReLU units,
      - more dropout, and finally
      - 10 softmax outputs for categories 0-9.

    Parameters
    ----------
    input_shape : tuple
        Shape of a single input image, e.g. (28, 28, 1).

    Returns
    -------
    tensorflow.keras.Model
        The compiled model.
    """
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',          # the notebook also suggests RMSprop
                  metrics=['accuracy'])
    return model


def train_model(model, train_images, train_labels, test_images, test_labels):
    """Fit the CNN on the training data.

    Returns
    -------
    history : tensorflow.keras.callbacks.History
        Training history (loss/accuracy per epoch).
    """
    history = model.fit(train_images, train_labels,
                        batch_size=BATCH_SIZE,
                        epochs=EPOCHS,
                        verbose=2,
                        validation_data=(test_images, test_labels))
    return history


def evaluate_model(model, test_images, test_labels):
    """Print the loss and accuracy of the model on the test set."""
    score = model.evaluate(test_images, test_labels, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


def main():
    """Run the full MNIST CNN pipeline."""
    (train_images, train_labels,
     test_images, test_labels, input_shape) = load_data()

    display_sample(1234, train_images, train_labels)

    model = build_model(input_shape)
    model.summary()

    train_model(model, train_images, train_labels, test_images, test_labels)
    evaluate_model(model, test_images, test_labels)


if __name__ == '__main__':
    main()