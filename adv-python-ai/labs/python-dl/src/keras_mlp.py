"""A Multi-Layer Perceptron (MLP) on the MNIST digit data set using Keras.

This program mirrors the ``Keras.ipynb`` notebook. It builds a two-layer
feed-forward neural network with the high-level Keras API and trains it to
recognize handwritten digits (0-9) from the MNIST data set.

Flow
----
1. Load the MNIST data set (60K train / 10K test images).
2. Flatten each 28x28 image into a 1-D vector of 784 pixels and normalize
   the pixel values into the [0, 1] range.
3. Convert the integer labels (0-9) into "one-hot" encoded vectors.
4. Build a ``Sequential`` model: an input layer of 784 features feeding into
   a ReLU hidden layer of 512 neurons, and a softmax output layer of 10 units.
5. Compile the model with categorical cross-entropy and the RMSprop optimizer.
6. Train for 10 epochs with a batch size of 100, validating on the test set.
7. Evaluate the final model and visualize some of the misclassified images.

Run it with::

    python src/keras_mlp.py

Note: training on a CPU-only TensorFlow build can take a few minutes.
"""

import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop

# Hyper-parameters
NUM_CLASSES = 10      # digits 0-9
BATCH_SIZE = 100
EPOCHS = 10


def load_data():
    """Load and normalize the MNIST data set.

    Returns
    -------
    (train_images, train_labels, test_images, test_labels) : tuple
        The training and test images (as flattened, normalized float
        arrays of shape (N, 784)) and their one-hot encoded labels
        (as arrays of shape (N, 10)).
    """
    (mnist_train_images, mnist_train_labels), \
        (mnist_test_images, mnist_test_labels) = mnist.load_data()

    # Flatten the 28x28 images into a single vector of 784 pixels.
    train_images = mnist_train_images.reshape(60000, 784)
    test_images = mnist_test_images.reshape(10000, 784)

    # Convert to float and normalize pixel values from [0, 255] to [0, 1].
    train_images = train_images.astype('float32') / 255
    test_images = test_images.astype('float32') / 255

    # One-hot encode the labels, e.g. the digit 1 becomes [0, 1, 0, ..., 0].
    train_labels = keras.utils.to_categorical(mnist_train_labels, NUM_CLASSES)
    test_labels = keras.utils.to_categorical(mnist_test_labels, NUM_CLASSES)

    return train_images, train_labels, test_images, test_labels


def display_sample(num, train_images, train_labels):
    """Render a single training sample so we can sanity-check the data.

    Parameters
    ----------
    num : int
        Index of the training sample to display.
    train_images : numpy.ndarray
        The flattened training images.
    train_labels : numpy.ndarray
        The one-hot encoded training labels.
    """
    # Print the one-hot array for this sample's label, then its digit.
    print(train_labels[num])
    label = train_labels[num].argmax(axis=0)

    # Reshape the 784 values back into a 28x28 image and plot it.
    image = train_images[num].reshape([28, 28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()


def build_model():
    """Construct the Keras ``Sequential`` MLP model.

    The network is deliberately simple: 784 inputs -> 512 ReLU neurons
    -> 10 softmax outputs. A dropout layer between them is included to
    reduce overfitting.

    Returns
    -------
    tensorflow.keras.Model
        The compiled model.
    """
    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(784,)))
    model.add(Dropout(0.2))
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    # Multiple categories => categorical cross-entropy loss. RMSprop is a
    # good general-purpose optimizer; try 'adam' as well.
    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])
    return model


def train_model(model, train_images, train_labels, test_images, test_labels):
    """Fit the model on the training data.

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


def show_misclassifications(model, test_images, test_labels, limit=1000):
    """Plot up to ``limit`` images that the model got wrong.

    A visual inspection of failures is useful to understand the kinds of
    samples that are genuinely hard to classify.
    """
    for x in range(limit):
        test_image = test_images[x, :].reshape(1, 784)
        predicted_cat = model.predict(test_image).argmax()
        label = test_labels[x].argmax()
        if predicted_cat != label:
            plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
            plt.imshow(test_image.reshape([28, 28]),
                       cmap=plt.get_cmap('gray_r'))
            plt.show()


def main():
    """Run the full MNIST MLP pipeline."""
    train_images, train_labels, test_images, test_labels = load_data()

    # Sanity-check the prepared data.
    display_sample(1234, train_images, train_labels)

    model = build_model()
    model.summary()

    train_model(model, train_images, train_labels, test_images, test_labels)
    evaluate_model(model, test_images, test_labels)
    show_misclassifications(model, test_images, test_labels)


if __name__ == '__main__':
    main()