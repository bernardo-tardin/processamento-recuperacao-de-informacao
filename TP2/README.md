# Inverted Index and Boolean Query Processor

This Python script implements a basic information retrieval system. It builds an inverted index from a collection of text files and provides functions to perform boolean queries (`AND`, `OR`, `NOT`) on that index.

### Core Concepts 💡

#### Inverted Index

The `matrizIndiceInvertido` function builds an inverted index, a fundamental data structure in search engines. Instead of listing terms by document, the index maps each term to a list of documents (called a posting list) in which it appears. This makes term lookups extremely fast.

  * Input: A list of text files (e.g., ['doc1.txt', 'doc2.txt']).

Output: A dictionary where each key is a term and the value is a list of document IDs (e.g., {'europe': [1, 2], 'book': [1]}).

Boolean Operations

The script includes optimized functions to combine these postings lists and answer complex queries. The AND and OR functions use an efficient merge algorithm that processes the lists in linear time.

AND(list1, list2): Returns the intersection of the two lists (documents containing both terms).

OR(list1, list2): Returns the union of the two lists (documents containing at least one of the terms).

NOT(list1, total_docs): Returns all documents that are not in the list.
