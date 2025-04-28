
import json
from educational_alife.ontology.ontology_extractor import OntologyExtractor
from educational_alife.stem_cells.stem_cell_generator import StemCellGenerator
from educational_alife.evolution.evolution_engine import OntologyAwareEvolutionEngine
from educational_alife.fitness.fitness_evaluator import FitnessEvaluator

# Step 1: Load sample textbook
with open('../samples/sample_learning_theories.txt', 'r', encoding='utf-8') as f:
    textbook_text = f.read()

# Step 2: Extract Ontology
ontology_extractor = OntologyExtractor()
ontology = ontology_extractor.extract_ontology(textbook_text)
ontology_extractor.save_ontology(ontology, output_file='../simulations/extracted_ontology.json')

# Step 3: Slice into Stem Cells
stem_cell_generator = StemCellGenerator(ontology)
stem_cells = stem_cell_generator.slice_textbook(textbook_text)
stem_cell_generator.save_to_json(stem_cells, output_file='../simulations/stem_cells_with_ontology.json')

# Step 4: Evolve for 5 Generations
evolution_engine = OntologyAwareEvolutionEngine(ontology, stem_cells)
evolution_engine.evolve(generations=5)
evolved_population = evolution_engine.get_population()

# Step 5: Evaluate Fitness
fitness_evaluator = FitnessEvaluator(ontology)
evaluated_population = fitness_evaluator.evaluate_population(evolved_population)
evaluated_population.sort(key=lambda x: x['fitness'], reverse=True)

# Step 6: Save results
with open('../simulations/final_evolved_population.json', 'w', encoding='utf-8') as f:
    json.dump([e['lo'] for e in evaluated_population], f, indent=2, ensure_ascii=False)

print("Simulation complete. Final evolved population saved!")
