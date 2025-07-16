# Boolean Retrieval Models in Python
This repository explores two fundamental models for building a boolean search engine, a cornerstone of Information Retrieval. It demonstrates the progression from a simple, conceptual model using an Incidence Matrix to the more scalable and standard approach using an Inverted Index.

## 🧠 Model 1: Incidence Matrix with Bitwise Operations
This model implements a boolean search engine using a classic incidence matrix. It's a straightforward, matrix-based approach ideal for understanding the core logic of boolean retrieval.

#### How It Works

1. Text Processing & Indexing:

* The script reads a collection of PDF documents.

* It tokenizes the text, converting it to lowercase and removing non-alphanumeric characters.

* An incidence matrix is built (as a Python dictionary), where rows represent a predefined set of terms and columns represent the documents. A cell contains 1 if a term is present in a document and 0 otherwise.

2. Query Processing:

* A user's query (e.g., `"philosophy AND (book OR work)"`) is parsed.

* Boolean operators (`AND`, `OR`, `NOT`) are cleverly mapped to Python's bitwise operators (`&`, `|`, `~`).

* Each term in the query is replaced by its corresponding row (bit vector) from the incidence matrix.

* The entire expression is evaluated using `eval()`, which performs the bitwise operations on the vectors to produce a final vector identifying the matching documents.

While effective for small document collections, this model becomes inefficient at scale, as the matrix can grow very large and sparse.

## 🚀 Model 2: Inverted Index with Merge Algorithms
This model implements a more practical and scalable boolean search engine using an inverted index, the standard data structure used in modern search systems.

#### How It Works

1. Index Construction:

* The script processes a collection of text files.

* It builds an inverted index (as a Python dictionary) that maps each term to a list of document IDs where it appears. This list is called a postings list.

* This structure is highly efficient as it only stores data for terms that actually exist, avoiding the sparsity problem of the incidence matrix.

2. Query Processing:

* Instead of bitwise operations on full vectors, this model uses highly efficient algorithms that operate directly on the postings lists.

* `AND`: An optimized merge algorithm finds the intersection of two postings lists in linear time.

* `OR`: A similar merge algorithm finds the union of two lists.

* `NOT`: A set difference operation identifies documents that are not in a given postings list.

This approach is significantly more memory-efficient and faster for large document collections, forming the foundation of real-world search engines.
