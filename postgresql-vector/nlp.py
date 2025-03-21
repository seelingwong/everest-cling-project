import spacy

nlp = spacy.load("en_core_web_sm")

query = "lightweight basketball sneakers for outdoor courts."
doc = nlp(query)

# Extract nouns and noun chunks
noun_chunks = [chunk.text for chunk in doc.noun_chunks]
# nouns = [token.text for token in doc if token.pos_ in ["NOUN"]]

# # Filtering: Remove adjectives and stopwords, keep key product-related nouns


# Analyze syntax
print("Noun phrases:", noun_chunks)
for token in doc:
    print(token.pos_, token.text)
nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
print("noun:", nouns)
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

filtered_phrases = [phrase for phrase in noun_chunks if any(
    noun in phrase for noun in nouns)]

# Step 4: Further refine the result by removing extra descriptive words
core_product = None
for phrase in filtered_phrases:
    words = phrase.split()
    clean_words = [word for word in words if word in nouns]  # Keep only nouns
    if clean_words:
        core_product = " ".join(clean_words)  # Convert back to string

print("Extracted Product Name:", core_product)
