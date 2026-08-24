# Deep Learning with Python

A collection of self-contained Python programs converted from the Jupyter
notebooks in [`notebooks/`](notebooks/). Each program is a standalone
script with proper module/function docstrings, section comments, and a
`main()` entry point, so the same code can be run from the command line,
imported as a library, or studied step by step.

## Contents

| Program | Source notebook | Problem it solves | Key techniques |
|---|---|---|---|
| [`src/keras_mlp.py`](src/keras_mlp.py) | `Keras.ipynb` | Handwritten digit recognition (MNIST) | Multi-layer perceptron with Keras |
| [`src/keras_cnn.py`](src/keras_cnn.py) | `Keras-CNN.ipynb` | Handwritten digit recognition (MNIST) | Convolutional neural network with Keras |
| [`src/keras_rnn.py`](src/keras_rnn.py) | `Keras-RNN.ipynb` | Sentiment analysis on IMDB movie reviews | LSTM recurrent neural network |
| [`src/tensorflow_nn.py`](src/tensorflow_nn.py) | `Tensorflow.ipynb` | Handwritten digit recognition (MNIST) | Raw TensorFlow 2, `GradientTape`, `tf.data` |
| [`src/q_learning.py`](src/q_learning.py) | `Q-Learning.ipynb` | The self-driving "Taxi" puzzle | Q-learning reinforcement learning |
| [`src/transfer_learning.py`](src/transfer_learning.py) | `TransferLearning.ipynb` | Classifying arbitrary photos | Transfer learning with pre-trained ResNet50 |
| [`src/tfidf.py`](src/tfidf.py) | `TF-IDF.py` | Finding the best-matching document for a term | TF-IDF with Spark MLlib |

## Installation

The programs use different frameworks, so install only what you need.

```bash
# Keras / TensorFlow programs (keras_mlp, keras_cnn, keras_rnn,
# tensorflow_nn, transfer_learning)
pip install tensorflow matplotlib numpy

# Q-Learning program
pip install gym numpy

# TF-IDF program
# Requires a working Spark installation + PySpark (run via spark-submit)
```

> **Note on versions:** `keras_rnn.py` and `q_learning.py` use
> legacy/version-dependent APIs (e.g. `gym.make("Taxi-v3").env`,
> `keras.preprocessing`). Adjust the version strings if your install
> reports the environment as unavailable.

## How to run

All programs print their results to the console:

```bash
python src/keras_mlp.py          # trains a 2-layer MLP on MNIST
python src/keras_cnn.py          # trains a CNN on MNIST
python src/keras_rnn.py          # trains an LSTM on IMDB reviews
python src/tensorflow_nn.py      # trains a raw-TF network on MNIST
python src/q_learning.py         # trains a Q-table for the Taxi game
python src/transfer_learning.py --image my_photo.jpg --image other.jpg
spark-submit src/tfidf.py        # needs a Spark cluster + data file
```

`transfer_learning.py` accepts the images you want to classify as
command-line arguments. All the other programs run end-to-end with no
arguments.

## Suggested learning flow

The programs form a natural progression from simple to advanced:

1. **`src/tensorflow_nn.py`** — start here to see how a neural network is
   built *by hand*: variables, weights/biases, forward pass, cross-entropy
   loss, and gradient descent via `GradientTape`. This is the foundation
   every later program hides behind a higher-level API.

2. **`src/keras_mlp.py`** — re-solves the exact same MNIST problem with
   the high-level Keras API (`Sequential`, `model.compile`, `model.fit`).
   Compare it with step 1 to appreciate how much boilerplate Keras removes.

3. **`src/keras_cnn.py`** — same problem again, but with convolutional
   layers (`Conv2D`, `MaxPooling2D`, `Dropout`). This improves accuracy
   from ~97% to >99% because CNNs are insensitive to *where* a pattern
   appears in the image.

4. **`src/keras_rnn.py`** — a different kind of data: sequential text.
   Uses an Embedding layer plus an LSTM to keep a "memory" of words, and
   predicts binary sentiment from full movie reviews (~80% accuracy with
   just the first 80 words of each review).

5. **`src/transfer_learning.py`** — no training at all: loads a ResNet50
   already trained on ImageNet and uses it to classify arbitrary photos
   into 1,000 categories.

6. **`src/q_learning.py`** — a completely different paradigm: reinforcement
   learning. Learns a Q-table over 10,000 simulated taxi trips with
   epsilon-greedy exploration, then plays the game using the learned policy.

7. **`src/tfidf.py`** — a text search technique rather than a neural
   network. Computes TF-IDF document vectors with Spark and answers which
   document best matches a query term.

## Data

- The MNIST data set (used by `keras_mlp.py`, `keras_cnn.py`, and
  `tensorflow_nn.py`) is downloaded automatically by Keras/TensorFlow on
  first run. Pre-downloaded copies also exist under [`data/MNIST_data/`](data/MNIST_data/).
- The IMDB reviews (used by `keras_rnn.py`) are downloaded automatically.
- `q_learning.py` creates its own simulated world via OpenAI Gym.
- `transfer_learning.py` downloads the ImageNet weights once (~100 MB).
- `tfidf.py` expects a tab-separated `subset-small.tsv` data file.

## Performance warning

`keras_cnn.py`, `keras_rnn.py`, and `tensorflow_nn.py` are compute-heavy.
Running them on a CPU can take a long time (each CNN epoch can take ~20
minutes) and will max out your CPU. To experiment quickly, lower the
`EPOCHS` / `TRAINING_STEPS` constants at the top of each file, and prefer a
GPU-accelerated TensorFlow build when you want the real results.
