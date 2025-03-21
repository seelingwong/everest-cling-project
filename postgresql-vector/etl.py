"""
This module performs ETL (Extract, Transform, Load) operations on product data.

Functions:
    clean_duplicate_data(): Reads product data from a JSON file, removes items with duplicate descriptions, 
                            and saves the cleaned data back to a JSON file.
    load_into_db(): Loads the cleaned product data from a JSON file into a PostgreSQL database.

Usage:
    Run this module as a script to initialize the database, clean the data, and load it into the database.
"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import DATABASE_URL, add_product, init_db

INPUT_FILE = 'data/sample.json'
OUTPUT_FILE = 'data/cleaned_sample.json'


def clean_duplicate_data():
    with open(INPUT_FILE, 'r') as file:
        data = json.load(file)

    # Remove items with duplicate descriptions
    unique_descriptions = set()
    cleaned_data = []

    for item in data:
        description = item.get('description')
        if description not in unique_descriptions:
            unique_descriptions.add(description)
            cleaned_data.append(item)

    # Save cleaned data back to file
    with open(OUTPUT_FILE, 'w') as file:
        json.dump(cleaned_data, file, indent=4)


def load_into_db():
    with open(OUTPUT_FILE, 'r') as file:
        cleaned_data = json.load(file)

    engine = create_engine(DATABASE_URL)

    with Session(engine) as session:
        for data in cleaned_data:
            name = data.get('name')
            description = data.get('description')
            category = data.get('category')
            price = data.get('price')

            add_product(session, name, description, category, price)


if __name__ == '__main__':
    init_db()
    clean_duplicate_data()
    load_into_db()
