 File-Encryption-and-Decryption

# 💳 Online Payment Fraud Detection Ensemble Model

This repository houses the code and resources for a machine learning project focused on building a robust system to detect fraudulent online payment transactions. The solution uses an Ensemble Model built from multiple powerful classifiers for high-accuracy risk assessment.

Project Explanation & Purpose

This project develops a high-performance system for online payment fraud detection. The core of the system is an Ensemble Model (a "super-model" combining three individual models: Logistic Regression, XGBoost, and Random Forest) trained to analyze the characteristics of financial transactions.

The model's purpose is to accurately assess the probability of fraud in real-time, allowing financial institutions to flag and stop malicious transfers. The accompanying Streamlit application provides an interactive platform for testing and validating the model's predictions using manually input transaction data.

🚀 Setup & Installation

Follow these steps to set up the project environment and run the application.

Step 1: Clone the Repository

git clone [YOUR_REPOSITORY_URL]
cd [YOUR_REPOSITORY_NAME]


Step 2: Create and Activate a Virtual Environment

It is best practice to install dependencies in a isolated environment (.venv).

For Windows:

python -m venv .venv
.\.venv\Scripts\activate


For macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate


Step 3: Download Data and Model Files

This project relies on a large dataset and a trained model file, which must be downloaded manually from the links below and placed into your project root directory.

Download Dataset: Place the downloaded file into the project root directory and ensure it is named new_data.csv.

Dataset Link: https://drive.google.com/file/d/127JqP3WGjBVihR-ZcUR86T3wwy3_g63v/view?usp=sharing

Download Trained Ensemble Model: Place the downloaded model file into the project root directory and ensure it is named Ensemble_Fraud_Detection_Model.joblib.

Model Link: https://drive.google.com/drive/folders/1m2o_gxVcRLGJLcpifdDhzzJfuK0djaof?usp=sharing (Look for the .joblib file in this folder).

Step 4: Install Dependencies

With your virtual environment activated, install all required Python libraries using the requirements.txt file.

pip install -r requirements.txt


Step 5: Run the Streamlit Application

Execute the main application file. This will open the interactive model tester in your web browser.

streamlit run app.py


📖 Model Training Resources (From Original Notebook)

The original model was built and trained using the following core steps and components:

Data Preprocessing

One-Hot Encoding: The categorical type column (CASH_OUT, TRANSFER, etc.) was converted into numerical features.

Feature Removal: Non-predictive identifier columns (nameOrig, nameDest) were removed.

Handling Imbalance: The XGBoost classifier was configured with scale_pos_weight=773 to account for the extreme rarity of fraudulent transactions.

Key Models

The final ensemble combines these three trained classifiers using a Soft Voting strategy:

Logistic Regression: Baseline linear model.

Random Forest Classifier: Tree-based ensemble, prone to overfitting but excellent feature representation.

XGBoost Classifier (Tuned): Gradient Boosting ensemble, the best performer in the individual model tests.

Evaluation Metric: ROC AUC Score

The primary metric used for evaluation is the Area Under the Receiver Operating Characteristic Curve (ROC AUC). This is essential for imbalanced datasets because it effectively measures the model's ability to correctly rank fraud vs. non-fraud transactions, regardless of the classification threshold.
