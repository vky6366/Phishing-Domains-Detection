# Phishing-Domains-Detection

![image 6](https://github.com/user-attachments/assets/5a5ec421-3ee8-4dda-a2ce-a4cfe7520975)
![image 1](https://github.com/user-attachments/assets/db260269-1722-48e4-813f-7d71ad19d53d)
![image 2](https://github.com/user-attachments/assets/9324bb59-8ca4-4031-8775-104dc47c6589)
![image 3](https://github.com/user-attachments/assets/ad4a6ad4-938e-480c-a9a6-7d726108dcdb)
![image 4](https://github.com/user-attachments/assets/26bf8866-7d8c-4046-98b1-c9f788a4de68)


# Phishing Domains Detection

Detect and classify phishing domains using machine learning. This repository provides tools, notebooks, and scripts for identifying malicious (phishing) domains based on features extracted from domain names and possibly other metadata. The project is intended for cybersecurity researchers, data scientists, and developers interested in automated phishing detection.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

Phishing is a prevalent threat where attackers use deceptive domain names to trick users. This project leverages data analysis and machine learning to build models capable of distinguishing phishing domains from legitimate ones, using features derived from the domain name and other information.

## Features

- Feature extraction from domain names (length, character composition, entropy, etc.)
- Preprocessing and cleaning of raw datasets
- Jupyter Notebooks for exploratory data analysis and modeling
- Multiple machine learning models for detection/classification
- Model evaluation and visualization
- Example scripts and usage documentation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vky6366/Phishing-Domains-Detection.git
   cd Phishing-Domains-Detection
   ```

2. **Install dependencies:**
   Most dependencies are listed in `requirements.txt`. Install them using pip:
   ```bash
   pip install -r requirements.txt
   ```
   Or, if you use JupyterLab/Notebook:
   ```bash
   pip install jupyter
   ```

## Usage

- **Jupyter Notebooks:**  
  Explore the notebooks in this repository to see step-by-step data analysis, feature engineering, and model building.
  ```bash
  jupyter notebook
  ```
  Then open and run the provided notebooks.

- **Python Scripts:**  
  Some features or model training steps may be available as standalone scripts (check the repo for `.py` files). Run them as:
  ```bash
  python script_name.py
  ```

## Data

- Use your own dataset or download publicly available phishing/legitimate domain lists.
- Typical format: CSV with at least columns like `domain` and `label` (`1` for phishing, `0` for legitimate).
- Place your dataset in a `data/` directory or as specified in the notebooks/scripts.

## Model Training

- Follow the instructions in the main notebook(s) to preprocess data, extract features, train models, and evaluate performance.
- You can experiment with different algorithms and feature sets by editing the notebooks.

## Technologies Used

- **Languages:** Jupyter Notebook, Python, Kotlin
- **Libraries:** pandas, scikit-learn, numpy, matplotlib, seaborn, etc.

## Contributing

Contributions, issues and feature requests are welcome!
- Fork the repository
- Create a new branch
- Submit a pull request

## License

This project is licensed under the MIT License.

---

**Author:** 
1. [Vishwakalyan Patil](https://github.com/vky6366)
2. [Akshay Sarapure](https://github.com/Codexyze)
