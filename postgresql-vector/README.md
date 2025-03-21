# PostgreSQL with Vector
This project will show how to use [tsvector](https://www.postgresql.org/docs/current/datatype-textsearch.html) and [pgvector](https://github.com/pgvector/pgvector).
And also show PostgreSQL to perform:
    - Full-text Search
    - Semantic Search
    - Hyprid Search

## Introduction to `tsvector` and `pgvector`

PostgreSQL offers powerful text search capabilities through the use of `tsvector` and `pgvector`. These features allow for efficient and flexible search functionalities within your database.

### `tsvector`

`tsvector` is a data type in PostgreSQL designed for full-text search. It stores lexemes (words) along with their positions in the document, enabling efficient text search operations.

#### Key Features:
- **Tokenization**: Breaks down text into tokens (words).
- **Stemming**: Reduces words to their root form.
- **Ranking**: Assigns relevance scores to search results.

### `pgvector`

`pgvector` is an extension for PostgreSQL that provides vector similarity search capabilities. It is particularly useful for applications involving machine learning and natural language processing, where data is often represented as vectors.

#### Key Features:
- **Vector Storage**: Stores high-dimensional vectors.
- **Similarity Search**: Finds vectors that are similar to a given query vector.
- **Indexing**: Supports indexing for fast similarity searches.

### Full-text Search

Full-text search allows you to search for documents that contain specific words or phrases. It uses `tsvector` to tokenize and index text, enabling efficient search and retrieval of relevant documents based on keyword matches.

### Semantic Search

Semantic search goes beyond keyword matching by understanding the meaning and context of the search query. It leverages `pgvector` to perform similarity searches, finding documents that are contextually related to the query even if they don't contain the exact keywords.

### Hybrid Search

Hybrid search combines full-text search and semantic search to provide more comprehensive search results. It uses both `tsvector` for keyword matching and `pgvector` for contextual similarity, offering a balanced approach to finding relevant documents.

## Setup Instructions

Follow these steps to set up the project:


### 1. Minimum Requirements

Ensure you have Python 3.12 installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Setup Virtual Environment

Create a virtual environment to manage project dependencies. Run the following commands in your terminal:

```sh
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Requirements

Install the required Python packages using `requirements.txt`:

```sh
pip install -r requirements.txt
```

### 4. Setup AWS SSO
    1. Configure SSO
    ```sh
    aws configure sso
    ```

    2. Fill in the start URL and region
    3. Will auto open browser and verify the code.
    4. Fill in the default region and output format as json.
    5. Fill in the profile name as AWS-local-sso.
    6. Run python aws-bedrock.py to verify sso is work.

### 5. Create .env file

Copy from .env.example to .env file, and fill in required variable.

### 6. Run ETL Script

Execute the ETL script to prepare your data:

```sh
python etl.py
```

### 6. Run Main Application

Finally, run the main application:

```sh
python main.py
```

## Next/Pending Tasks

### Integrate spaCy with User Query

The current pending task is to integrate [spaCy](https://spacy.io/) with user queries to increase the accuracy of full-text search. spaCy is a powerful NLP library that can enhance text processing and understanding, leading to more accurate search results.

By integrating spaCy, we aim to improve the relevance and accuracy of search results, providing a better user experience.