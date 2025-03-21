"""
This module defines SQLAlchemy ORM models for the PostgreSQL database used in the Everest Cling project.

Classes:
    Base: A base class for declarative class definitions.
    Product: A class representing the 'products' table in the database.

Attributes:
    Product.id (int): The primary key for the product, auto-incremented.
    Product.name (str): The name of the product, with a maximum length of 255 characters.
    Product.description (str): A text description of the product.
    Product.category (str): The category of the product.
    Product.price (float): The price of the product, cannot be null.
    Product.search_vector (TSVECTOR): A tsvector column for full-text search.
    Product.embedding (Vector): A vector column for storing embeddings with 1536 dimensions.
    Product.aws_embedding (Vector): A vector column for storing AWS embeddings with 1024 dimensions.
    Product.created_at (TIMESTAMP): The timestamp when the product was created, defaults to the current time.
"""
from sqlalchemy import TEXT, TIMESTAMP, Integer, String, Float, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.dialects.postgresql import TSVECTOR
from pgvector.sqlalchemy import Vector


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    description = mapped_column(TEXT)
    category = mapped_column(TEXT)
    price = mapped_column(Float, nullable=False)
    search_vector = mapped_column(TSVECTOR)
    embedding = mapped_column(Vector(1536))
    aws_embedding = mapped_column(Vector(1024))
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, server_default=func.now())
