"""Handwritten digit recognition using raw TensorFlow 2 (no Keras layers).

This program mirrors the ``Tensorflow.ipynb`` notebook. Instead of using
the high-level Keras API, it builds a multi-layer perceptron from scratch
with low-level TensorFlow 2: explicit weight/bias variables, ``tf.data``
batches, a ``GradientTape`` for automatic differentiation, and a manually
implemented SGD optimization loop.

Flow
----
1. Load and prepare the MNIST data set: flatten images to 784 features,
   normalize pixels, one-hot encode labels for loss computation.
2. Wrap the data in a ``tf.data.Dataset`` that is shuffled and batched.
3. Define network weights/biases for a 784 -> 512 (sigmoid) -> 10 (softmax)
   architecture using ``tf.Variable``.
4. Implement ``neural_net``, ``cross_entropy``, ``accuracy``, and
   ``run_optimization`` (gradient descent via ``GradientTape``).
5. Train for 3000 steps, logging loss/accuracy every 100 steps.
6. Evaluate test accuracy and visualize misclassified test images.

Run it with::

    python src/tensorflow_nn.py

Expect roughly 93% test accuracy. You can improve on this by tuning the
hyper-parameters (learning rate, hidden size, batch size) or by adding
extra hidden layers.
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

# MNIST data set parameters
NUM_CLASSES = 10  # total classes (0-9 digits)
NUM_FEATURES = 784  # data features (28 * 28)

# Training hyper-parameters
LEARNING_RATE = 0.001
TRAINING_STEPS = 3000
BATCH_SIZE = 250
DISPLAY_STEP = 100

# Network parameters
N_HIDDEN = 512  # number of neurons in the hidden layer


def load_data():
    """Load MNIST and prepare the training/test tensors.

    Returns
    -------
    (x_train, x_test, y_train, y_test) : tuple
        Images flattened to 784 features and normalized to [0, 1],
        plus the corresponding integer labels.
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Convert to float32.
    x_train, x_test = np.array(x_train, np.float32), np.array(x_test, np.float32)

    # Flatten images to 1-D vectors of 784 features (28 * 28).
    x_train, x_test = (
        x_train.reshape([-1, NUM_FEATURES]),
        x_test.reshape([-1, NUM_FEATURES]),
    )

    # Normalize image values from [0, 255] to [0, 1].
    x_train, x_test = x_train / 255.0, x_test / 255.0

    return x_train, x_test, y_train, y_test


def build_train_dataset(x_train, y_train):
    """Wrap the training data in a shuffled, batched ``tf.data.Dataset``.

    The dataset repeats forever, so the training loop can simply ``take``
    as many batches as it wants.
    """
    train_data = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    train_data = train_data.repeat().shuffle(60000).batch(BATCH_SIZE).prefetch(1)
    return train_data


def create_weights():
    """Create the trainable weight and bias variables for each layer.

    A random-value generator initializes the weights so they start with
    small, non-zero values. Returns a dict of the layer weights and a
    dict of the layer biases.
    """
    random_normal = tf.initializers.RandomNormal()
    weights = {
        "h": tf.Variable(random_normal([NUM_FEATURES, N_HIDDEN])),
        "out": tf.Variable(random_normal([N_HIDDEN, NUM_CLASSES])),
    }
    biases = {
        "b": tf.Variable(tf.zeros([N_HIDDEN])),
        "out": tf.Variable(tf.zeros([NUM_CLASSES])),
    }
    return weights, biases


def neural_net(input_data, weights, biases):
    """Feed input data forward through the network to produce probabilities.

    - Hidden layer: input x weights + bias, then sigmoid activation.
    - Output layer: hidden x weights + bias, then softmax to normalize the
      logits into a probability distribution over the 10 classes.

    Parameters
    ----------
    input_data : tensor
        A batch of input images.
    weights : dict
        Layer weight variables.
    biases : dict
        Layer bias variables.

    Returns
    -------
    tensor
        Softmax probabilities for each class.
    """
    # Hidden fully-connected layer with 512 neurons.
    hidden_layer = tf.add(tf.matmul(input_data, weights["h"]), biases["b"])
    # Apply sigmoid for non-linearity.
    hidden_layer = tf.nn.sigmoid(hidden_layer)

    # Output fully-connected layer, one neuron per class.
    out_layer = tf.matmul(hidden_layer, weights["out"]) + biases["out"]
    # Apply softmax to normalize logits into a probability distribution.
    return tf.nn.softmax(out_layer)


def cross_entropy(y_pred, y_true):
    """Cross-entropy loss between predicted probabilities and true labels.

    The true labels are first one-hot encoded, and predictions are clipped
    to avoid ``log(0)`` errors. Cross-entropy penalizes confident, wrong
    classifications far more than ones that are close.

    Returns
    -------
    tensor
        The mean cross-entropy over the batch.
    """
    # Encode the label into a one-hot vector.
    y_true = tf.one_hot(y_true, depth=NUM_CLASSES)
    # Clip prediction values to avoid log(0).
    y_pred = tf.clip_by_value(y_pred, 1e-9, 1.0)
    # Compute cross-entropy.
    return tf.reduce_mean(-tf.reduce_sum(y_true * tf.math.log(y_pred)))


def run_optimization(x, y, weights, biases, optimizer):
    """Run one step of SGD on a single batch using ``GradientTape``.

    The ``GradientTape`` records every operation on trainable variables so
    that gradients can be computed automatically (the modern replacement for
    TensorFlow 1.x sessions).
    """
    # Wrap the computation in a GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        pred = neural_net(x, weights, biases)
        loss = cross_entropy(pred, y)

    # Collect all trainable variables.
    trainable_variables = list(weights.values()) + list(biases.values())

    # Compute the gradients of the loss w.r.t. those variables.
    gradients = g.gradient(loss, trainable_variables)

    # Update the weights and biases following the gradients.
    optimizer.apply_gradients(zip(gradients, trainable_variables))


def accuracy(y_pred, y_true):
    """Fraction of predictions that match the true labels.

    Returns
    -------
    tensor
        Mean accuracy over the batch (0.0 to 1.0).
    """
    # Predicted class is the index of the highest score in the prediction.
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)


def train(x_train, y_train, x_test, y_test):
    """Run the full training loop and return the trained weights/biases."""
    train_data = build_train_dataset(x_train, y_train)
    weights, biases = create_weights()

    # Stochastic gradient descent optimizer with the given learning rate.
    optimizer = tf.keras.optimizers.SGD(LEARNING_RATE)

    # Train for the given number of steps.
    for step, (batch_x, batch_y) in enumerate(train_data.take(TRAINING_STEPS), 1):
        run_optimization(batch_x, batch_y, weights, biases, optimizer)

        if step % DISPLAY_STEP == 0:
            # here we compute the predictions for the current batch
            pred = neural_net(batch_x, weights, biases)
            # compute the loss for the current batch
            loss = cross_entropy(pred, batch_y)
            # compute the accuracy for the current batch
            acc = accuracy(pred, batch_y)
            print("Training epoch: %i, Loss: %f, Accuracy: %f" % (step, loss, acc))

    return weights, biases


def evaluate(x_test, y_test, weights, biases):
    """Print the accuracy of the trained model on the held-out test set."""
    pred = neural_net(x_test, weights, biases)
    print("Test Accuracy: %f" % accuracy(pred, y_test))


def visualize_misclassifications(x_test, y_test, weights, biases, n_images=200):
    """Plot misclassified test images along with the model's guesses."""
    test_images = x_test[:n_images]
    test_labels = y_test[:n_images]
    predictions = neural_net(test_images, weights, biases)

    for i in range(n_images):
        model_prediction = np.argmax(predictions.numpy()[i])
        if model_prediction != test_labels[i]:
            plt.imshow(np.reshape(test_images[i], [28, 28]), cmap="gray_r")
            plt.show()
            print("Original Labels: %i" % test_labels[i])
            print("Model prediction: %i" % model_prediction)


def main():
    """Run the full low-level TensorFlow MNIST pipeline."""
    x_train, x_test, y_train, y_test = load_data()

    # Visualize a sample so we know what the data looks like.
    plt.imshow(x_train[1000].reshape([28, 28]), cmap=plt.get_cmap("gray_r"))
    plt.title("Sample: 1000  Label: %d" % y_train[1000])
    plt.show()

    # Train the model and return the learned weights and biases.
    weights, biases = train(x_train, y_train, x_test, y_test)
    # Evaluate the trained model on the test set and visualize misclassifications.
    evaluate(x_test, y_test, weights, biases)
    # Visualize some misclassified test images along with the model's guesses.
    visualize_misclassifications(x_test, y_test, weights, biases)

    # can you add a logic to predict a single image using the trained model?
    single_image = x_test[0:1]  # Select a single image
    single_label = y_test[0:1]  # Select the corresponding label
    predicted_label = np.argmax(neural_net(single_image, weights, biases))
    print("Original Label: %i" % single_label[0])
    print("Single Image Prediction: %i" % predicted_label)

    # can i download an image from the internet and predict it using the trained model?
    # Yes, but the model only understands inputs that look exactly like its
    # training data: a bright digit on a dark background, 28x28 pixels,
    # flattened to 784 features and scaled to [0, 1]. A downloaded PNG is
    # none of those things yet, so it has to be pre-processed first.
    # ``data/images/mnist-3.0.1.png`` is a 3x3 grid of digits, so it is also
    # split into its nine tiles before each one is predicted.
    predict_image_file("data/images/mnist-3.0.1.png", weights, biases)


def load_grayscale_image(image_path):
    """Read an image file from disk as a 2-D grayscale array in [0, 1].

    Parameters
    ----------
    image_path : str or Path
        Path to the image. A relative path is resolved against the project
        root, so the script works no matter which directory it is run from.

    Returns
    -------
    ndarray
        Float32 array of shape (height, width) where 0.0 is black and
        1.0 is white.
    """
    # Local import so this block needs nothing from the top of the file.
    from pathlib import Path

    path = Path(image_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[1] / path

    # plt.imread handles PNG/JPG and returns floats in [0, 1] for PNGs.
    image = plt.imread(path)

    # Drop the alpha channel and average R, G, B down to a single gray value.
    if image.ndim == 3:
        image = image[..., :3].mean(axis=-1)

    # JPEGs come back as uint8 in [0, 255], so rescale those to [0, 1].
    image = image.astype(np.float32)
    if image.max() > 1.0:
        image = image / 255.0

    return image


def split_into_digit_tiles(gray_image, dark_threshold=0.5, fill_fraction=0.3):
    """Split a grid-of-digits screenshot into one array per digit.

    The sample image is a matplotlib figure: nine dark squares laid out on a
    white page, each with a caption underneath. Rows and columns that are
    mostly dark belong to the squares, while the white gaps and the thin
    caption text are not, so scanning the dark-pixel fraction per row and
    per column recovers the tile boundaries.

    Returns
    -------
    list of ndarray
        One crop per digit, or ``[gray_image]`` if no grid was detected
        (i.e. the file already contains a single digit).
    """
    dark = gray_image < dark_threshold

    def dark_bands(fractions, min_size=8):
        """Group consecutive mostly-dark rows (or columns) into bands."""
        bands = []
        start = None
        for index, fraction in enumerate(fractions):
            if fraction > fill_fraction and start is None:
                start = index
            elif fraction <= fill_fraction and start is not None:
                if index - start >= min_size:
                    bands.append((start, index))
                start = None
        if start is not None and len(fractions) - start >= min_size:
            bands.append((start, len(fractions)))
        return bands

    row_bands = dark_bands(dark.mean(axis=1))
    column_bands = dark_bands(dark.mean(axis=0))

    # No dark blocks: treat the whole picture as one digit.
    if not row_bands or not column_bands:
        return [gray_image]

    return [
        gray_image[row_start:row_end, col_start:col_end]
        for row_start, row_end in row_bands
        for col_start, col_end in column_bands
    ]


def to_mnist_input(tile):
    """Convert one digit crop into a single MNIST-style input row.

    This reproduces how the original MNIST images were built:

    1. Make the digit bright on a dark background (invert if needed).
    2. Crop away the empty border so only the ink is left.
    3. Resize the ink so its longest side is 20 pixels.
    4. Paste it into a 28x28 canvas, centered on its center of mass.
    5. Flatten to 784 features already scaled to [0, 1].

    Returns
    -------
    ndarray
        Float32 array of shape (1, 784), ready for ``neural_net``.
    """
    ink = tile

    # MNIST is white-on-black. A mostly bright crop is a dark digit on light
    # paper, so invert it.
    if ink.mean() > 0.5:
        ink = 1.0 - ink

    # Crop to the bounding box of the ink.
    mask = ink > 0.25
    if mask.any():
        rows = np.where(mask.any(axis=1))[0]
        columns = np.where(mask.any(axis=0))[0]
        ink = ink[rows[0] : rows[-1] + 1, columns[0] : columns[-1] + 1]

    # Scale the longest side to 20 pixels, keeping the aspect ratio.
    height, width = ink.shape
    scale = 20.0 / max(height, width)
    new_height = max(1, int(round(height * scale)))
    new_width = max(1, int(round(width * scale)))
    resized = tf.image.resize(ink[..., None], [new_height, new_width]).numpy()[..., 0]

    # Center the digit in a 28x28 canvas using its center of mass.
    canvas = np.zeros([28, 28], np.float32)
    ys, xs = np.mgrid[0:new_height, 0:new_width]
    total_ink = resized.sum()
    center_y = round((ys * resized).sum() / total_ink) if total_ink > 0 else 14
    center_x = round((xs * resized).sum() / total_ink) if total_ink > 0 else 14
    top = int(np.clip(14 - center_y, 0, 28 - new_height))
    left = int(np.clip(14 - center_x, 0, 28 - new_width))
    canvas[top : top + new_height, left : left + new_width] = resized

    # Same shape and value range as a row of x_test.
    return np.clip(canvas, 0.0, 1.0).reshape([1, NUM_FEATURES])


def predict_image_file(image_path, weights, biases):
    """Predict every digit in a downloaded image with the trained model.

    Prints the predicted digit and the model's confidence for each digit
    found in the file, and plots the pre-processed 28x28 inputs so it is
    obvious what the network actually saw.
    """
    gray_image = load_grayscale_image(image_path)
    tiles = split_into_digit_tiles(gray_image)
    print("Downloaded image: %s (%d digit(s) found)" % (image_path, len(tiles)))

    # Pre-process every tile, then predict them all in one batch.
    batch = np.concatenate([to_mnist_input(tile) for tile in tiles], axis=0)
    probabilities = neural_net(batch, weights, biases).numpy()

    predictions = np.argmax(probabilities, axis=1)
    confidences = np.max(probabilities, axis=1)
    for index, (digit, confidence) in enumerate(zip(predictions, confidences)):
        print(
            "  Digit %d prediction: %i (confidence %.2f)" % (index, digit, confidence)
        )

    # Show what the network was fed, labelled with its prediction.
    columns = int(np.ceil(np.sqrt(len(tiles))))
    rows = int(np.ceil(len(tiles) / columns))
    figure, axes = plt.subplots(rows, columns, figsize=(2 * columns, 2 * rows))
    for axis, image_row, digit in zip(np.ravel([axes]), batch, predictions):
        axis.imshow(image_row.reshape([28, 28]), cmap="gray_r")
        axis.set_title("Predicted: %i" % digit)
        axis.axis("off")
    # Hide any unused subplot in the last row.
    for axis in np.ravel([axes])[len(tiles) :]:
        axis.axis("off")
    figure.suptitle("Predictions for the downloaded image")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
