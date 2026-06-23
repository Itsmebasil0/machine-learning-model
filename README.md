# machine-learning-model
this is a machine learning model project for predicting charges of insurance according to the data of the person
# 🏥 Health Insurance Premium Predictor

An end-to-end Machine Learning web application that estimates an individual's annual health insurance premium based on their demographic and health characteristics. 

This project transitions a data science exploration workflow from a Google Colab notebook into a clean, interactive **Streamlit** web application.

---

## 🚀 Live Demo
*(Once you deploy it on Streamlit Cloud, you can paste your link here!)*
👉 [Live Web App Link Coming Soon]()

---

## ✨ Features
* **Interactive UI:** Built with Streamlit, allowing users to input data using simple sliders, numerical inputs, and dropdown selectors.
* **Smart Data Translation:** Automates data preprocessing behind the scenes (maps categorical features, handles automated BMI classification, and applies a pre-trained `StandardScaler`).
* **Machine Learning Brain:** Powered by a **Random Forest Regressor** trained on historical insurance datasets, achieving a **86.53% prediction accuracy (R² Score)**.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Visualization/EDA:** Seaborn, Matplotlib
* **Web Framework:** Streamlit

---

## 📂 Project Structure
```text
├── app.py                 # Streamlit frontend & prediction logic
├── insurance_model.pkl    # Trained Random Forest Regressor model
├── scaler.pkl             # Fitted StandardScaler object for inputs
└── README.md              # Project documentation
