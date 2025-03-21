"""
This module provides functionality to generate text embeddings using OpenAI's API.

Functions:
    get_embedding(text: str) -> list:
        Generates an embedding for the given text using OpenAI's embedding model.

Dependencies:
    - os: For accessing environment variables.
    - dotenv: For loading environment variables from a .env file.
    - openai: For interacting with OpenAI's API.

Usage:
    Ensure that the environment variable 'OPENAI_API_KEY' is set in your .env file.
    Call the `get_embedding` function with the text you want to embed.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_embedding(text):
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = "text-embedding-3-small"

    # Using openai to do embeddings
    response = openai_client.embeddings.create(input=text, model=model)
    return response.data[0].embedding
