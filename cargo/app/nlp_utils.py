from transformers import pipeline

def extract_entities(text):
    nlp = pipeline("ner")
    entities = nlp(text)
    return entities
