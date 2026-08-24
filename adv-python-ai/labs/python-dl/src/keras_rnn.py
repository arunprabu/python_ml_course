"""Sentiment analysis on IMDB movie reviews using an LSTM RNN in Keras.

This program mirrors the ``Keras-RNN.ipynb`` notebook (inspired by the
``imdb_lstm.py`` example that ships with Keras). It trains a recurrent
neural network to "read" full-text movie reviews and predict whether the
author liked the movie, based on the review text.

Understanding written language requires keeping track of all the words in
a sentence, so we use an LSTM (Long Short-Term Memory) cell - a recurrent
layer that keeps a "memory" of the words that came before as it reads the
review over time. LSTM cells are used instead of plain recurrent cells
because we don't want to "forget" words too quickly.

Flow
----
1. Load the IMDB data set, keeping only the 20,000 most popular words.
2. Inspect the raw data: reviews are sequences of integers (word indices),
   labels are binary (0 = disliked, 1 = liked).
3. Pad/truncate every review to its first 80 words so the RNN doesn't blow
   up on long inputs.
4. Build the model: Embedding(20000, 128) -> LSTM(128, dropout) ->
   Dense(1, sigmoid).
5. Compile with binary cross-entropy and the Adam optimizer.
6. Train for 15 epochs with a batch size of 32.
7. Evaluate the final model on the test set.

Run it with::

    python src/keras_rnn.py

Warning: this will take a very long time to run, even on a fast PC!
Consider lowering ``EPOCHS`` if you just want a quick smoke test.
"""

from tensorflow.keras.datasets import imdb
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import sequence

# Hyper-parameters
MAX_FEATURES = 20000   # only keep the 20,000 most popular words
MAX_LEN = 80           # limit each review to its first 80 words
BATCH_SIZE = 32
EPOCHS = 15
EMBED_SIZE = 128       # dimension of the dense word embeddings


def load_data():
    """Load and pad the IMDB movie review data.

    The data set already converts words to integer indices and provides
    binary sentiment labels (0 = negative, 1 = positive). Reviews are
    truncated/padded to ``MAX_LEN`` words.

    Returns
    -------
    (x_train, y_train, x_test, y_test) : tuple
        Padded review sequences and their binary labels.
    """
    print('Loading data...')
    (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=MAX_FEATURES)

    # RNNs can blow up on long inputs, so cap every review at 80 words.
    x_train = sequence.pad_sequences(x_train, maxlen=MAX_LEN)
    x_test = sequence.pad_sequences(x_test, maxlen=MAX_LEN)

    return x_train, y_train, x_test, y_test


def build_model():
    """Construct the LSTM sentiment model.

    - Embedding layer: converts the integer word indices into dense vectors
      of fixed size (128), better suited for a neural network.
    - LSTM layer: the recurrent layer itself, with dropout to avoid the
      overfitting RNNs are particularly prone to.
    - Dense(1, sigmoid): boils everything down to a binary 0/1 classification.

    Returns
    -------
    tensorflow.keras.Model
        The compiled model.
    """
    model = Sequential()
    model.add(Embedding(MAX_FEATURES, EMBED_SIZE))
    model.add(LSTM(EMBED_SIZE, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(1, activation='sigmoid'))

    # Binary classification => binary cross-entropy loss.
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def train_model(model, x_train, y_train, x_test, y_test):
    """Fit the LSTM model on the training reviews.

    RNNs, like CNNs, are very resource heavy. Keeping the batch size
    relatively small is the key to enabling this to run on a PC at all.
    """
    model.fit(x_train, y_train,
              batch_size=BATCH_SIZE,
              epochs=EPOCHS,
              verbose=2,
              validation_data=(x_test, y_test))


def evaluate_model(model, x_test, y_test):
    """Print the loss and accuracy of the model on the test set."""
    score, acc = model.evaluate(x_test, y_test,
                                batch_size=BATCH_SIZE,
                                verbose=2)
    print('Test score:', score)
    print('Test accuracy:', acc)


def main():
    """Run the full IMDB sentiment analysis pipeline."""
    x_train, y_train, x_test, y_test = load_data()

    # Quick look at the raw data: a review is a vector of word indices,
    # and a label is 0 or 1.
    print('First training review (word indices):', x_train[0])
    print('First training label:', y_train[0])

    model = build_model()

    train_model(model, x_train, y_train, x_test, y_test)
    evaluate_model(model, x_test, y_test)


if __name__ == '__main__':
    main()