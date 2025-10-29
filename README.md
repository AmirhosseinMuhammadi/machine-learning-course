# Foundations of Representation Learning
Foundations of Representation Learning is a narrative-driven course that unfolds like a novel. Unlike traditional categorization-based approaches (supervised vs unsupervised), this course follows a conceptual storyline grounded in modern representation learning principles. The curriculum emphasizes end-to-end projects and practical implementation over theoretical categorization.

## Course Narrative
This course takes you on a journey through the fundamental concepts of representation learning, building each chapter upon the previous one to create a cohesive understanding of how modern AI systems learn and represent information.

The course is organized into the following chapters, each expressed in separate Jupyter notebooks.
- Chapter 1: Introdoction
- Chapter 2: Python Essentials
- Chapter 3: Linearity
- Chapter 4: Non-linearity
- Chapter 5: Curse of Dimensionality
- Chapter 6: Unsupervised Learning
- Chapter 7: Sequences and Creativity
- Chapter 8: Agentic AI

## Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package installer)

## Installation & Setup
The following steps can be done to set up the project on a local machine.

1. Cloning the Repository
```bash
git clone https://github.com/AmirhosseinMuhammadi/representation-learning-foundations.git
cd representation-learning-foundations
```

2. Setting up a Virtual Environment
```bash
# Creating a virtual environment
python3 -m venv ml_venv

# Activate it
source ml_venv/bin/activate     #Linux/Mac
ml_venv\Scripts\activate        # Windows

# Deactivate the virtual environment when no longer is needed
deactivate
```

3. Installing Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Launching Jupyter Notebook/Lab
```bash
jupyter notebook
# or
jupyter lab
```

## Project Structure
```text
representation-learning-foundations/
├── api/              # API application (Flask/FastAPI)
├── notebooks/        # Exploration and analysis
│   ├── chapter_01_introduction.ipynb
│   ├── chapter_02_python_essentials.ipynb
│   ├── chapter_03_linearity.ipynb
│   ├── chapter_04_non_linearity.ipynb
│   ├── chapter_05_curse_of_dimensionality.ipynb
│   ├── chapter_06_unsupervised_learning.ipynb
│   ├── chapter_07_sequences_and_creativity.ipynb
│   └── chapter_08_agentic_ai.ipynb
|
|*** figures/          # External images used in notebooks
├── data/
│   ├── raw/           # Raw data files
│   └── processed/     # Processed data files
│
├── src/               # Source code modules and production-ready ML code
├── tests/             # Shared tests
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```
--- figures

## Requirements
The project requires the following Python packages which are also specified in `requirements.txt`:
```text
jupyter
numpy
pandas
matplotlib
seaborn
scikit-learn
keras
torch
tensorflow
flask
fastapi[standard]
```
## Learning Approach: Narrative-Driven Methodology
This course breaks from traditional ML syllabus by:

- Storyline Progression: Concepts build upon each other in a logical narrative flow
- Practical Focus: Each chapter includes hands-on implementations
- Modern Perspective: Emphasis on representation learning as the foundation
- Project-Based: End-to-end projects reinforce conceptual understanding

## Development
1. Adding New Dependencies
```bash
pip install package_name
pip freeze > requirements.txt
```

## contributions
It is possible submit pull requests, report bugs, or suggest new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Additional Resources
References are provided at the end of each chapter and are recommended for studing more.
