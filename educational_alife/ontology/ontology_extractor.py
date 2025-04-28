
import re
import json
from rake_nltk import Rake
import nltk

class OntologyExtractor:
    def __init__(self, max_phrases_per_section=5):
        self.rake = Rake()
        self.max_phrases = max_phrases_per_section

    def extract_ontology(self, text):
        paragraphs = self.split_into_paragraphs(text)
        ontology = {}
        current_topic = "general"

        for para in paragraphs:
            if self.is_heading(para):
                current_topic = self.clean_heading(para)
                ontology[current_topic] = []
            else:
                keyphrases = self.extract_keyphrases(para)
                ontology.setdefault(current_topic, []).extend(keyphrases)

        cleaned_ontology = {k: list(set(v)) for k, v in ontology.items() if v}
        return cleaned_ontology

    def split_into_paragraphs(self, text):
        paragraphs = re.split(r'\n\s*\n', text)
        return [p.strip() for p in paragraphs if p.strip()]

    def is_heading(self, para):
        heading_patterns = [
            r'chapter\s+\d+', r'section\s+\d+(\.\d+)*', r'^#\s+', r'^\d+\.\d+'
        ]
        for pattern in heading_patterns:
            if re.match(pattern, para.lower()):
                return True
        return len(para.strip().split()) < 6

    def clean_heading(self, heading):
        heading = heading.lower()
        heading = re.sub(r'chapter\s+\d+', '', heading)
        heading = re.sub(r'section\s+\d+(\.\d+)*', '', heading)
        heading = re.sub(r'^#\s+', '', heading)
        heading = re.sub(r'^\d+\.\d+', '', heading)
        return heading.strip()

    def extract_keyphrases(self, text):
        self.rake.extract_keywords_from_text(text)
        phrases = self.rake.get_ranked_phrases()
        return phrases[:self.max_phrases]

    def save_ontology(self, ontology, output_file='extracted_ontology.json'):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(ontology, f, indent=2, ensure_ascii=False)
    