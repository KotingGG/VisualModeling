# VisualModeling

[![Python](https://img.shields.io/badge/Python-3.13.7+-blue.svg?style=for-the-badge)](https://python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

## About This Project

This project is about modeling different objects in the python programming language with different rendering approaches. 

So far implemented:
- Atom modeling:
according to the Schröndireng equation, the UI shows areas where electrons are more likely to appear. The color indicates the greater or lesser chance of an electron appearing at that location. The atom rotates along a certain axis. 

- Modeling in the terminal: 
a 3D object from symbols is depicted. Has rotation around a specific axis.

When you start any rendering, you are given a choice in the terminal of which object.

This repository is solely for the sake of learning and the interest of creating renders in different conditions and different objects. 

(TODO: Document all this, please)

## Quick Start
**Prerequisites**
- Python 3.13+

### Installation & Run
**Clone and set up the project:**
```
git clone https://github.com/KotingGG/GameAgnosticCognitivePlayer.git
cd Game-Agnostic-Cognitive-Player
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Activation of virtual space**
```bash
venv\Scripts\activate 
```

**Run The Project:**

1. **Atom:**
Project launch
```bash
py src/Atom/main.py
```

2. **Terminal Render:**
Project launch
```bash
py src/TerminalRender/main.py
```
