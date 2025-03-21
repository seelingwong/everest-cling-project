"""
This module provides functions to initialize a PostgreSQL database, add products, and perform various types of searches including semantic search, AWS semantic search, full-text search, and hybrid search.

Functions:
- init_db(): Initializes the database, creates necessary extensions, tables, and indexes.
- add_product(session, name, description, category, price): Adds a product to the database with embeddings and search vectors.
- semantic_search(query_text): Performs semantic search using embeddings.
- aws_semantic_search(query_text): Performs semantic search using AWS embeddings.
- full_text_search(query_text): Performs full-text search using PostgreSQL's full-text search capabilities.
- hybrid_search(query_text): Performs a hybrid search combining full-text search and semantic search.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import Index, create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import to_tsvector
from llm import get_embedding
from aws_llm import get_aws_embedding
from models import Base, Product

load_dotenv(override=True)


DATABASE_URL = f"postgresql+psycopg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"


def init_db():
    print(DATABASE_URL)
    engine = create_engine(DATABASE_URL)

    with Session(engine) as session:
        # Create the extension
        session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        session.commit()

        # Create the table
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        # Create the index
        embedding_index = Index(
            'embedding_index',
            Product.embedding,
            postgresql_using='hnsw',
            postgresql_with={'m': 16, 'ef_construction': 64},
            postgresql_ops={'embedding': 'vector_l2_ops'}
        )

        embedding_index.create(engine)
        aws_embedding_index = Index(
            'aws_embedding_index',
            Product.aws_embedding,
            postgresql_using='hnsw',
            postgresql_with={'m': 16, 'ef_construction': 64},
            postgresql_ops={'aws_embedding': 'vector_l2_ops'}
        )

        aws_embedding_index.create(engine)

        search_index = Index(
            'search_index',
            Product.search_vector,
            postgresql_using='gin'
        )
        search_index.create(engine)


def add_product(session, name, description, category, price):

    embedding_input = f"{name} {description} {category} {price}"
    embedding = get_embedding(embedding_input)
    aws_embedding = get_aws_embedding(embedding_input)

    search_input = f"{name} {description} {category}"
    search_vector = to_tsvector("english", search_input)

    product = Product(
        name=name,
        description=description,
        category=category,
        price=price,
        search_vector=search_vector,
        embedding=embedding,
        aws_embedding=aws_embedding
    )
    session.add(product)
    session.commit()

    return product


def semantic_search(query_text):
    """Perform semantic search using embeddings."""
    query_embedding = get_embedding(query_text)

    sql = text("""
        SELECT p.*, p.embedding <=> :query_embedding AS score
        FROM products p
        ORDER BY score ASC
        LIMIT 10;
    """)

    engine = create_engine(DATABASE_URL, echo=True)

    with Session(engine) as session:
        results = session.execute(sql, {
            "query_embedding": str(query_embedding)
        }).fetchall()

        return results


def aws_semantic_search(query_text):
    """Perform semantic search using AWS embeddings."""
    query_embedding = get_aws_embedding(query_text)

    sql = text("""
        SELECT p.*, p.aws_embedding <=> :query_embedding AS score
        FROM products p
        ORDER BY score ASC
        LIMIT 10;
    """)

    engine = create_engine(DATABASE_URL, echo=True)

    with Session(engine) as session:
        results = session.execute(sql, {
            "query_embedding": str(query_embedding)
        }).fetchall()

        return results


def full_text_search(query_text):
    """Perform full-text search using FTS."""
    sql = text("""
        SELECT p.*, ts_rank(p.search_vector, to_tsquery('english',:query_text)) AS score
        FROM products p
        WHERE p.search_vector @@ to_tsquery('english',:query_text)
        ORDER BY score DESC
        LIMIT 10;
    """)

    engine = create_engine(DATABASE_URL, echo=True)

    with Session(engine) as session:
        results = session.execute(sql, {
            "query_text": query_text.replace(" ", " & ")
        }).fetchall()

        return results


def hybrid_search(query_text):
    """Perform hybrid search using FTS + Semantic Search."""
    query_embedding = get_embedding(query_text)

    sql = text("""
        SELECT p.*, 
               1 - (p.embedding <=> :query_embedding) AS semantic_score, 
               ts_rank(p.search_vector, to_tsquery('english',:query_text)) AS text_score,
               (0.7 * (1 - (p.embedding <=> :query_embedding)) + 0.3 * ts_rank(p.search_vector, to_tsquery('english', :query_text))) AS final_score
        FROM products p
        WHERE p.search_vector @@ to_tsquery('english',:query_text)
        ORDER BY final_score DESC
        LIMIT 10;
    """)

    engine = create_engine(DATABASE_URL, echo=True)

    with Session(engine) as session:
        results = session.execute(sql, {
            "query_embedding": str(query_embedding),
            # Convert to tsquery format
            "query_text": query_text.replace(" ", " & ")
        }).fetchall()

        return results
