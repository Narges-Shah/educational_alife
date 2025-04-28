
# Educational ALife Ecosystem

This project simulates an artificial life ecosystem for educational content, inspired by AVIDA, biological evolution, and cosmological models.

## Project Structure

- `/ontology/`
  - `ontology_extractor.py`: Extracts major topics and subtopics from a textbook.
- `/stem_cells/`
  - `stem_cell_generator.py`: Slices the textbook into coherent stem cell Learning Objects (LOs).
- `/evolution/`
  - `evolution_engine.py`: Evolves LOs through mutation and differentiation while respecting Ontology constraints.
- `/fitness/`
  - `fitness_evaluator.py` (planned): Evaluates LOs based on Ontology depth, structure quality, and metabolic tasks.
- `/simulations/`
  - `run_simulation.py`: Runs full evolutionary cycles and tracks generation history.
- `/docs/`
  - `educational_universe_theory.md`: Document explaining the scientific model.

## Setup

```bash
pip install -r requirements.txt
```

## How to Run

1. Extract Ontology from a textbook using `ontology_extractor.py`.
2. Slice textbook into stem cells using `stem_cell_generator.py`.
3. Run evolutionary simulations using `run_simulation.py`.
4. Observe evolving LOs across generations!

## Key Inspirations

- Biological Evolution
- Artificial Life (AVIDA)
- Knowledge Ontology Expansion
- Competency-Driven Educational Systems

Enjoy exploring the growth of your own educational universe! 🌱📚✨
