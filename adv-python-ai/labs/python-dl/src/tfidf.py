"""Term Frequency - Inverse Document Frequency (TF-IDF) with PySpark.

This program mirrors the ``TF-IDF.py`` script from the notebooks folder.
It computes TF-IDF vectors for a collection of documents and then answers
a classic search-style question: which document best matches a query term?

TF-IDF weighs a term by how often it appears in a document (TF) while
down-weighting terms that show up across many documents (IDF), so rare,
distinctive terms end up with higher scores. The Spark MLlib
``HashingTF`` / ``IDF`` transformers compute this over an RDD of documents.

Flow
----
1. Start a local SparkContext.
2. Load documents from a TSV file (one document per line), split each
   line into fields, and treat field index 3 as the document text.
3. Hash the words in each document into a fixed number of hash buckets
   to produce sparse term-frequency vectors.
4. Fit an IDF transformer (ignoring terms in fewer than 2 documents) and
   transform the TF vectors into TF-IDF vectors.
5. Compute the TF-IDF relevance of a query term (e.g. "Gettysburg")
   for every document and print the document with the highest score.

Run it with::

    spark-submit src/tfidf.py

or, if you run PySpark from a script, make sure a SparkContext exists
first. Requires a working PySpark / Spark installation.
"""

from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF, IDF

# Configuration
APP_NAME = "SparkTFIDF"
DATA_FILE = "subset-small.tsv"   # tab-separated file, field 3 is the text
NUM_HASH_BUCKETS = 100000        # hash buckets (sparse vector size)
MIN_DOC_FREQ = 2                 # ignore terms appearing in fewer docs
QUERY_TERM = "Gettysburg"        # the term we are looking for


def load_documents(sc):
    """Load the raw documents from the TSV file.

    Returns
    -------
    (documents, document_names) : (RDD, RDD)
        ``documents`` is an RDD of word lists (one per document), and
        ``document_names`` is an RDD of the corresponding names.
    """
    # Load documents (one per line).
    raw_data = sc.textFile(DATA_FILE)
    fields = raw_data.map(lambda x: x.split("\t"))

    # Document text lives in field 3; split it into words.
    documents = fields.map(lambda x: x[3].split(" "))

    # Store the document names for later.
    document_names = fields.map(lambda x: x[1])

    return documents, document_names


def compute_tfidf(sc):
    """Hash term frequencies and fit/transform them into TF-IDF vectors.

    Returns
    -------
    (hashing_tf, tfidf, document_names) : (HashingTF, RDD, RDD)
        The hashing transformer (needed to hash query terms), the RDD of
        sparse TF-IDF vectors (one per document), and the document names.
    """
    documents, document_names = load_documents(sc)

    # Hash the words in each document to their term frequencies.
    # 100K hash buckets just to save some memory.
    hashing_tf = HashingTF(NUM_HASH_BUCKETS)
    tf = hashing_tf.transform(documents)

    # At this point ``tf`` is an RDD of sparse vectors representing each
    # document, where each value maps to the term frequency of each unique
    # hash value. Now compute the TF*IDF of each term in each document.
    tf.cache()
    idf = IDF(minDocFreq=MIN_DOC_FREQ).fit(tf)
    tfidf = idf.transform(tf)

    return hashing_tf, tfidf, document_names


def best_document_for_term(hashing_tf, tfidf, document_names, term):
    """Find the document with the highest TF-IDF score for ``term``.

    The term is hashed with the same ``HashingTF`` used on the documents,
    then each document's TF-IDF vector is indexed by that hash value and
    zipped with the document names to find the best match.

    Returns
    -------
    tuple
        The (score, document_name) of the best matching document.
    """
    # Figure out what hash value the query term maps to.
    term_tf = hashing_tf.transform([term])
    term_hash_value = int(term_tf.indices[0])

    # Extract the TF*IDF score for that hash value from every document.
    term_relevance = tfidf.map(lambda x: x[term_hash_value])

    # Zip in the document names so we can see which document is which.
    zipped_results = term_relevance.zip(document_names)

    return zipped_results.max()


def main():
    """Run the full TF-IDF pipeline and print the best matching document."""
    # Boilerplate Spark setup: local master for a single machine.
    conf = SparkConf().setMaster("local").setAppName(APP_NAME)
    sc = SparkContext(conf=conf)

    hashing_tf, tfidf, document_names = compute_tfidf(sc)

    print("Best document for %s is:" % QUERY_TERM)
    print(best_document_for_term(hashing_tf, tfidf, document_names, QUERY_TERM))

    sc.stop()


if __name__ == '__main__':
    main()