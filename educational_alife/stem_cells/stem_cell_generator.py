
import uuid
import re
import json
from rake_nltk import Rake
import nltk

class StemCellGenerator:
    def __init__(self, ontology, min_words=80, max_words=300, min_keywords=2):
        self.ontology = ontology
        self.min_words = min_words
        self.max_words = max_words
        self.min_keywords = min_keywords
        self.rake = Rake()
        self.flat_ontology = self.flatten_ontology(ontology)

    def flatten_ontology(self, ontology):
        flat = set()
        for parent, children in ontology.items():
            flat.add(parent.lower())
            flat.update([c.lower() for c in children])
        return flat

    def slice_textbook(self, text):
        paragraphs = self.split_into_paragraphs(text)
        stem_cells = []

        for para in paragraphs:
            words = nltk.word_tokenize(para)
            if self.min_words <= len(words) <= self.max_words:
                keywords = self.extract_keywords(para)
                assigned_concepts = self.match_keywords_to_ontology(keywords)

                if len(keywords) >= self.min_keywords and assigned_concepts:
                    lo = {
                        'id': str(uuid.uuid4()),
                        'type': 'Text',
                        'content': para.strip(),
                        'keywords': ",".join(keywords),
                        'ontology_concepts': list(assigned_concepts),
                        'interactivity_type': 'expositive',
                        'generation': 0
                    }
                    stem_cells.append(lo)
        return stem_cells

    def split_into_paragraphs(self, text):
        paragraphs = re.split(r'\n\s*\n', text)
        return [p.strip() for p in paragraphs if p.strip()]

    def extract_keywords(self, text, n=5):
        self.rake.extract_keywords_from_text(text)
        phrases = self.rake.get_ranked_phrases()
        return phrases[:n]

    def match_keywords_to_ontology(self, keywords):
        matches = set()
        for kw in keywords:
            cleaned_kw = kw.lower().strip()
            for concept in self.flat_ontology:
                if concept in cleaned_kw or cleaned_kw in concept:
                    matches.add(concept)
        return matches

    def save_to_json(self, stem_cells, output_file='stem_cells_with_ontology.json'):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(stem_cells, f, indent=2, ensure_ascii=False)
    