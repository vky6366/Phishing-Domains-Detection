# 🛡️ Phishing  Domain Detection


Detect and classify phishing domains using machine learning. This repository provides tools, notebooks, and scripts for identifying malicious (phishing) domains based on features extracted from domain names and possibly other metadata. The project is intended for cybersecurity researchers, data scientists, and developers interested in automated phishing detection.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Technologies Used](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Phishing URL Predictor** is a smart security app designed to help users detect malicious and phishing websites before clicking on them.  
Don't let cyber threats catch you off guard.  
🔍 This app uses **machine learning** to analyze URLs in real-time and determine if they're safe or potentially harmful.

## 🚀 Application Implementation
<div align="center">
  <img src="https://github.com/user-attachments/assets/df84f81b-b375-4e55-9af4-eb06c5f41760" />
</div>




## Features

- Feature extraction from domain names (length, character composition, entropy, etc.)
- Preprocessing and cleaning of raw datasets
- Jupyter Notebooks for exploratory data analysis and modeling
- Multiple machine learning models for detection/classification
- Model evaluation and visualization
- Example scripts and usage documentation
---
  ## Application Features

- 🌐 URL input and analysis interface
- ⚙️ Backend Flask API integrated with a Machine Learning model
- 📡 Retrofit API communication
- 🧠 Smart ML predictions for phishing detection
- 🔔 Instant UI feedback on URL safety
- 📱 Built with Jetpack Compose and MVVM Architecture
- 🛡️ Option to contact cybersecurity support when a URL is unsafe

---

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
  python app_server.py
  ```

## Data

- Dataset: https://www.kaggle.com/datasets/ndarvind/phiusiil-phishing-url-dataset
- Typical format: CSV with at least columns like `domain` and `label` (`1` for phishing, `0` for legitimate).
- Place your dataset in a `data/` directory or as specified in the notebooks/scripts.

## Model Training

- Follow the instructions in the main notebook(s) to preprocess data, extract features, train models, and evaluate performance.
- You can experiment with different algorithms and feature sets by editing the notebooks.

## 📈 Model Performance

The model was trained using **Stochastic Gradient Descent (SGD)** with the following performance:

- **Accuracy**: 99.69%
- **Precision**: 1.00 (for both classes)
- **Recall**: 0.99 (for class 0), 1.00 (for class 1)
- **F1-Score**: 1.00

> Dataset size: 2,35,370 samples

## Tech Stack

### 🎨 Frontend (Android App)
- **Kotlin**
- **Jetpack Compose** – Modern UI toolkit
- **MVVM Architecture** – Clean and scalable code separation
- **Retrofit** – API communication with Flask backend

### 🧪 Backend
- **Flask (Python)** – Lightweight API server
- **Stochastic Gradient Descent (SGD)** – SGD was chosen for its scalability with large datasets and its fast convergence, providing excellent results with minimal tuning.
- **RESTful API** – Endpoint to handle URL predictions

---

## 📲 App Flow

1. **Splash Screen**: Shows app branding.
2. **Home Screen**: User enters a suspicious URL.
3. **Prediction Request**: URL is sent to the Flask backend via Retrofit.
4. **Processing**: ML model evaluates the URL.
5. **Result**: UI shows whether the URL is safe ✅ or unsafe ❌.
6. **Action**: If unsafe, the user can tap **Contact CyberSecurity** for help.

## Contributing

Contributions, issues and feature requests are welcome!
- Fork the repository
- Create a new branch
- Submit a pull request

## License

This project is licensed under the [MIT LICENSE](LICENSE) .

---

**Author:** 
1. [Vishwakalyan Patil](https://github.com/vky6366)
2. [Akshay Sarapure](https://github.com/Codexyze)
