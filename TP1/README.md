# Boolean Search Engine for PDFs

This project is a simple implementation of a boolean search engine in Python. The script can process a collection of `.pdf` documents, identify the presence of predefined terms, and respond to a boolean query to find the relevant documents.

### How It Works 🔎
The process is divided into two main parts: document indexing and query processing.

1. Indexing and Tokenization

    *  The script reads three specified PDF files.

    * For each file, it extracts all the text, converts it to lowercase, and removes all non-alphanumeric characters.

    * The clean text is then split into "tokens" (words), and only the unique tokens are kept.

2. Incidence Matrix and Query Processing

    * An incidence matrix (represented as a Python dictionary) is created, where rows are a set of predefined terms and columns represent the documents. The value 1 indicates that the term exists in the document, while 0 indicates its absence.

    * The user's query (e.g., `"philosophy AND ( book OR work )"`) is processed.

    * The boolean operators `AND`, `OR`, and `NOT` are converted to their corresponding bitwise operators in Python (`&`, `|`, `~`).

    * Each term in the query is replaced by its corresponding bit vector from the incidence matrix.

    * The resulting expression is evaluated using the `eval()` function, which performs the bitwise operations to find the documents that satisfy the query.

    * Finally, the script prints the names of the PDF files that match the search result.
