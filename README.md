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
python3 -m venv ml_venv
source ml_venv/bin/activate     #Linux/Mac
ml_venv\Scripts\activate        # Windows
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
│
├── data/
│   ├── raw/           # Raw data files
│   └── processed/     # Processed data files
│
├── src/               # Source code modules and production-ready ML code
├── tests/             # Shared tests
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file

## Requirements
The project requires the following Python packages which are also specified in `requirements.txt`:
```text
jupyter>=1.0.0
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
seaborn>=0.11.0
scikit-learn>=1.0.0
torch>=1.9.0
torchvision>=0.10.0
tensorflow>=2.6.0
plotly>=5.3.0
ipywidgets>=7.6.0
tqdm>=4.62.0
```
