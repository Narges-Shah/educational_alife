
import random
from copy import deepcopy

class OntologyAwareEvolutionEngine:
    def __init__(self, ontology, initial_population, keyword_threshold_formal=5, keyword_threshold_pedagogic=8):
        self.ontology = ontology
        self.population = initial_population
        self.keyword_threshold_formal = keyword_threshold_formal
        self.keyword_threshold_pedagogic = keyword_threshold_pedagogic

    def mutate(self, lo):
        new_lo = deepcopy(lo)
        new_lo['content'] += " (Expanded with an additional example.)"

        if random.random() < 0.3:
            additional_concepts = self.get_related_concepts(new_lo['ontology_concepts'])
            if additional_concepts:
                new_concept = random.choice(additional_concepts)
                current_keywords = set(new_lo['keywords'].split(','))
                current_keywords.add(new_concept)
                new_lo['keywords'] = ",".join(current_keywords)
                new_lo['ontology_concepts'].append(new_concept)

        return new_lo

    def check_differentiation_condition(self, lo):
        keyword_count = len(lo['keywords'].split(','))
        if keyword_count >= self.keyword_threshold_pedagogic:
            return 'pedagogic'
        elif keyword_count >= self.keyword_threshold_formal:
            return 'formal'
        else:
            return None

    def formal_differentiation(self, lo):
        new_type = random.choice(['Image', 'Video', 'Audio'])
        new_lo = deepcopy(lo)
        new_lo['id'] = self.generate_new_id()
        new_lo['type'] = new_type
        new_lo['content'] = f"{new_type} representation derived from text."
        return new_lo

    def pedagogic_differentiation(self, lo):
        new_lo = deepcopy(lo)
        new_lo['id'] = self.generate_new_id()
        new_lo['type'] = 'Quiz'
        new_lo['interactivity_type'] = 'active'
        new_lo['content'] = "Quiz question based on main concepts."
        return new_lo

    def get_related_concepts(self, current_concepts):
        related = set()
        for concept in current_concepts:
            for parent, children in self.ontology.items():
                if concept == parent:
                    related.update(children)
                if concept in children:
                    related.add(parent)
                    related.update(children)
        related.difference_update(current_concepts)
        return list(related)

    def evolve(self, generations=1):
        for _ in range(generations):
            new_population = []
            for lo in self.population:
                new_lo = self.mutate(lo)
                diff_type = self.check_differentiation_condition(new_lo)
                if diff_type == 'formal':
                    diff_lo = self.formal_differentiation(new_lo)
                    new_population.append(diff_lo)
                elif diff_type == 'pedagogic':
                    diff_lo = self.pedagogic_differentiation(new_lo)
                    new_population.append(diff_lo)
                new_population.append(new_lo)
            self.population = new_population

    def generate_new_id(self):
        import uuid
        return str(uuid.uuid4())

    def get_population(self):
        return self.population
    