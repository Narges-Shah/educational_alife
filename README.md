# 🌌 Educational ALife Ecosystem

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Docs](https://img.shields.io/badge/Docs-Sphinx-green.svg)

**An Artificial Life Simulator for Growing Smart Learning Objects.**  
*Inspired by Biological Evolution, AVIDA, and the Big Bang.*

---

## 🚀 Project Description

Educational ALife is a living, evolving simulation system where Learning Objects (LOs) mutate, differentiate, specialize, and compete to survive — based on semantic, pedagogic, and ontological fitness.

Built from real textbooks, the system slices knowledge into "stem cells," lets them evolve into rich educational resources like quizzes, videos, summaries, and more — simulating a Big Bang of learning ecosystems.

---

## ✨ Key Features

- 📚 Ontology-based semantic evolution
- 🧬 Ontology-Aware mutations and differentiations
- 📈 Fitness evaluation based on educational value
- 🌱 Educational Metabolic Functions (Ontological Depth as Energy)
- 📦 Modular and professionally structured like AVIDA
- 🧪 Full Sphinx Documentation and Examples
- 🛠 Installable as a Python Package

---

## 🗂 Project Structure

```
/ontology/     → Ontology Extractor
/stem_cells/   → Textbook Slicer into Stem Cell LOs
/evolution/    → Evolution Engine
/fitness/      → Fitness Evaluator
/simulations/  → Run and Save Evolutionary Cycles
/samples/      → Sample Textbook: Learning Theories
/examples/     → Full Run Example Script
/docs/         → Sphinx Documentation
README.md, requirements.txt, setup.py, environment.yml
```

---

## 🛠 How to Install

First, clone the repository:

```bash
git clone https://github.com/Narges-Shah/educational_alife.git
cd educational_alife
```

Create the environment:

```bash
conda env create -f environment.yml
conda activate educational_alife
```

Or simply install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run a Full Simulation

From the `/examples/` directory:

```bash
python full_run_example.py
```

This will:
- Extract Ontology
- Slice textbook into Stem Cells
- Evolve them for 5 generations
- Evaluate Fitness
- Save the results!

---

## 📚 Documentation

You can generate the full documentation locally:

```bash
cd docs
sphinx-build -b html . _build/html
```

Or view live docs (coming soon via ReadTheDocs!).

---

## 📈 Sample Results

Starting from "Learning Theories White Paper", the system slices it into Learning Object stem cells, evolves them into specialized quizzes, summaries, and resources — showing real, semantic knowledge evolution over generations.

---

## 🤝 Contributing

Contributions are warmly welcome! 🌱  
Open an Issue, Suggest Improvements, Submit Pull Requests!

---

## 📝 License

This project is licensed under the **MIT License**.

---

*"Grow the seeds of knowledge into thriving forests of learning."* 🌳

---
