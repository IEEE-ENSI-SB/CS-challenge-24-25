# TunSecure-AI: An AutoML and Federated Learning Framework for Zero-Touch Network Anomaly Detection

![Dashboard Screenshot](https://raw.githubusercontent.com/IEEE-ENSI-SB/CS-challenge-24-25/main/cappppp.png)

[![Watch the Demo Video](https://raw.githubusercontent.com/IEEE-ENSI-SB/CS-challenge-24-25/main/video_thumbnail.png)](https://github.com/IEEE-ENSI-SB/CS-challenge-24-25/blob/main/CS.mp4)



## Table of Contents

- [Abstract](#abstract)
- [Dashboard Video](#dashboard-video)
- [Project Pipeline](#project-pipeline)
  - [1. Data Analysis and Preprocessing](#1-data-analysis-and-preprocessing)
    - [Data Cleaning](#data-cleaning)
    - [Handling Missing Values](#handling-missing-values)
    - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [2. AutoML Pipeline and Procedures](#2-automl-pipeline-and-procedures)
    - [Automated Data Pre-Processing](#automated-data-pre-processing)
    - [Automated Feature Engineering](#automated-feature-engineering)
    - [Automated Model Selection](#automated-model-selection)
    - [Hyper-Parameter Optimization](#hyper-parameter-optimization)
    - [Automated Model Ensemble](#automated-model-ensemble)
- [Implementation](#implementation)
  - [Machine Learning Algorithms](#machine-learning-algorithms)
  - [Data Balancing Methods](#data-balancing-methods)
  - [Feature Selection Methods](#feature-selection-methods)
  - [Optimization/AutoML Algorithms](#optimizationautoml-algorithms)
  - [Ensemble Learning Algorithms](#ensemble-learning-algorithms)
  - [Cybersecurity Script](#cybersecurity-script)
- [Installation](#installation)
- [Usage](#usage)
- [Datasets](#datasets)
- [Code](#code)
- [Authors](#authors)
- [License](#license)
- [References](#references)

## Abstract

As cyber threats grow in complexity and frequency, there is an urgent need for advanced cybersecurity solutions capable of adapting to evolving challenges. We introduce **TunSecure-AI**, an innovative framework that addresses emerging cybersecurity issues through a Zero-Touch Network (ZTN) architecture powered by Automated Machine Learning (AutoML) and Federated Learning (FL). TunSecure-AI creates a decentralized intrusion detection system that optimizes model selection and tuning while preserving data privacy across distributed networks. Our advanced monitoring dashboard enables real-time threat detection and automated response capabilities. Validation results demonstrate the system’s scalability and effectiveness, achieving an F1-score of 99.8% on the CICIDS2017 dataset and handling large network deployments efficiently. This positions Tunisia as a pioneer in next-generation cybersecurity solutions, contributing to a safer digital environment.

## Dashboard Video

Watch our [**Dashboard Demonstration Video**](https://www.example.com/path-to-your-dashboard-video.mp4) to see TunSecure-AI in action.

## Project Pipeline

Our project follows a structured pipeline to ensure efficient and effective intrusion detection. The pipeline consists of two main phases: **Data Analysis and Preprocessing** and **AutoML Pipeline and Procedures**.

### 1. Data Analysis and Preprocessing

Before diving into the AutoML processes, thorough data analysis and preprocessing are essential to ensure the quality and reliability of the dataset.

#### Data Cleaning

- **Removing Duplicates**: Identified and removed duplicate rows to maintain data integrity.
- **Handling Infinite Values**: Replaced infinite values in critical features with `NaN` to standardize the dataset.

#### Handling Missing Values

- **Identifying Missing Values**: Detected missing values in key features such as `Flow Bytes/s` and `Flow Packets/s`.
- **Imputing Missing Values**: Filled missing values using the median to preserve data distribution without introducing bias.

#### Exploratory Data Analysis (EDA)

- **Visualization**: Utilized bar charts, boxplots, and histograms to understand feature distributions and identify outliers.
- **Insights**: Identified non-normal distributions and the presence of outliers in key features, guiding further preprocessing steps.

### 2. AutoML Pipeline and Procedures

The AutoML pipeline automates various stages of the machine learning workflow, enhancing efficiency and model performance.

#### Automated Data Pre-Processing

Ensures that the dataset is balanced to prevent bias in model training.

- **Data Balancing**: Employed Tabular Variational Autoencoder (TVAE) to generate synthetic samples for minority classes, mitigating class imbalance.

#### Automated Feature Engineering

Enhances feature quality by selecting and creating the most relevant features.

- **Feature Importance Averaging**: Aggregated feature importance scores from multiple tree-based models to select the most significant features, reducing dimensionality and improving model performance.

#### Automated Model Selection

Selects the best-performing machine learning model from a pool of candidates.

- **Model Pool**: Includes Decision Tree (DT), Random Forest (RF), Extra Trees (ET), XGBoost, LightGBM, and CatBoost.
- **Selection Criteria**: Evaluated models based on performance metrics to identify the optimal model for intrusion detection.

#### Hyper-Parameter Optimization

Optimizes model hyperparameters to enhance performance.

- **Bayesian Optimization with Tree-structured Parzen Estimator (BO-TPE)**: Efficiently explored the hyperparameter space to identify optimal configurations, improving model accuracy and efficiency.

#### Automated Model Ensemble

Combines multiple models to improve overall prediction accuracy and robustness.

- **Optimized Confidence-based Stacking Ensemble (OCSE)**: Integrated predictions from selected models based on their confidence levels, enhancing final prediction accuracy and reliability.

## Implementation

### Machine Learning Algorithms

Our framework employs a diverse set of machine learning algorithms to ensure robust intrusion detection capabilities:

- **Decision Tree (DT)**
- **Random Forest (RF)**
- **Extra Trees (ET)**
- **XGBoost**
- **LightGBM**
- **CatBoost**

### Data Balancing Methods

- **Tabular Variational Autoencoder (TVAE)**: Generates synthetic data to balance classes, improving model training on imbalanced datasets.

### Feature Selection Methods

- **Feature Importance Averaging**: Aggregates feature importance from multiple models to identify and select the most significant features.

### Optimization/AutoML Algorithms

- **Bayesian Optimization with Tree-structured Parzen Estimator (BO-TPE)**: Optimizes hyperparameters by modeling the distribution of promising hyperparameters, enabling efficient search and selection.

### Ensemble Learning Algorithms

- **Stacking**: Combines multiple base models by training a meta-model to make final predictions.
- **Confidence-based Stacking**: Weighs base model predictions based on their confidence scores, enhancing ensemble performance.

### Cybersecurity Script

Included in the repository is a Python script named `cybersecurity.py`. This script is designed to block malicious destinations from receiving packets, enhancing network security by preventing unwanted or harmful traffic from reaching targeted sources.

- **Functionality**:
  - **Packet Blocking**: Identifies and blocks packets from specified malicious sources.
  - **Integration**: Can be integrated with existing security infrastructure to provide automated defense mechanisms.
  - **Customization**: Allows for specifying targets and conditions under which packets should be blocked.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip

### Clone the Repository

```bash
git clone https://github.com/IEEE-ENSI-SB/CS-challenge-24-25.git
cd CS-challenge-24-25
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: If you encounter issues with specific packages, ensure you have the latest versions or consult the package documentation.

## Usage

### Running the AutoML Pipeline

1. **Prepare the Data**: Ensure the datasets are downloaded and placed in the designated directory.

2. **Execute the Notebook**:
   - Open the Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Navigate to `CIC IDS 2017 AutoML.ipynb` or `5G NIDD Auto ML.ipynb` and run the cells sequentially.

3. **Visualize Results**: Utilize the dashboard for real-time monitoring and threat detection.

### Example Workflow

1. **Data Cleaning and Preprocessing**: Clean the dataset by removing duplicates and handling missing values.
2. **Feature Engineering**: Select and transform features to enhance model performance.
3. **Model Training and Selection**: Train multiple models and select the best-performing one.
4. **Hyper-Parameter Optimization**: Optimize model parameters for optimal performance.
5. **Model Ensemble**: Combine models to improve prediction accuracy and robustness.

### Running the Cybersecurity Script

To execute the cybersecurity script that blocks malicious traffic:

```bash
python cybersecurity.py
```

**Note**: Ensure you have the necessary permissions and configurations to run network-related scripts on your system.

## Datasets

Our framework utilizes the following datasets:

1. **CICIDS2017 Dataset**: A comprehensive dataset for intrusion detection.
   - **Download Link**: [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)

2. **5G-NIDD Dataset**: Focuses on non-IP traffic specific to 5G environments.
   - **Download Link**: [5G-NIDD](https://ieee-dataport.org/documents/5g-nidd-comprehensive-network-intrusion-detection-dataset-generated-over-5g-wireless)

## Code

The repository includes the following key notebooks:

- [`CIC IDS 2017 AutoML.ipynb`](https://github.com/IEEE-ENSI-SB/CS-challenge-24-25/blob/main/CS-challenge-24-25/CIC%20IDS%202017%20AutoML.ipynb): AutoML pipeline for the CICIDS2017 dataset.
- [`5G NIDD Auto ML.ipynb`](https://github.com/IEEE-ENSI-SB/CS-challenge-24-25/blob/main/CS-challenge-24-25/5G%20NIDD%20Auto%20ML.ipynb): AutoML pipeline for the 5G-NIDD dataset.

Additionally, the `cybersecurity.py` script is located in the root directory and can be used to block malicious traffic as described in the [Cybersecurity Script](#cybersecurity-script) section.

You can find these notebooks in the [**CS-challenge-24-25**](https://github.com/IEEE-ENSI-SB/CS-challenge-24-25/tree/main/CS-challenge-24-25) directory.

## Authors

- **Aymen Masmoudi**  
  National School of Computer Science, Manouba, Tunisia  
  IEEE ENSI Student Branch, Computer Science SBC, Manouba, Tunisia  
  [aymen.masmoudi@example.com](mailto:aymen.masmoudi@ensi-uma.tn)

- **Riadh Belgacem**  
  National School of Computer Science, Manouba, Tunisia  
  IEEE ENSI Student Branch, Computer Science SBC, Manouba, Tunisia  
  [riadh.belgacem@example.com](mailto:riadh.belgacem@ensi-uma.tn)

- **Nour Chakroun**  
  National School of Computer Science, Manouba, Tunisia  
  IEEE ENSI Student Branch, Computer Science SBC, Manouba, Tunisia  
  [nour.chakroun@example.com](mailto:nour.chakroun@ensi-uma.tn)

## License

This project is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material as long as appropriate credit is given.

## References

1. Li Yang, Abdallah Shami. "Towards Autonomous Cybersecurity: An Intelligent AutoML Framework for Autonomous Intrusion Detection." *Workshop on Autonomous Cybersecurity (AutonomousCyber 2024), ACM CCS 2024*.
2. [CICIDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)
3. [5G-NIDD Dataset](https://ieee-dataport.org/documents/5g-nidd-comprehensive-network-intrusion-detection-dataset-generated-over-5g-wireless)
4. Masmoudi, A., Belgacem, R., & Chakroun, N. "TunSecure-AI: An AutoML and Federated Learning Framework for Zero-Touch Network Anomaly Detection." *IEEE Data Descriptor Article Template*, VOLUME00, 2024.

---

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

**Note**: Replace placeholder links (e.g., `https://www.example.com/path-to-your-dashboard-video.mp4` and `https://www.example.com/path-to-your-dashboard-screenshot.png`) with actual URLs to your resources.
