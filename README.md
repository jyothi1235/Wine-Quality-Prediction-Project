# 🍷 Wine Quality Prediction System

🔗 **Live App:** https://jyothi1235-wine-quality-prediction-project-app-lj0gak.streamlit.app/

---

## 📌 Project Overview

This project is an **end-to-end Machine Learning application** that predicts whether a wine is **Good or Bad** based on its physicochemical properties such as acidity, pH, alcohol content, and sulphates.

The model is deployed as an interactive web application using Streamlit, allowing users to input wine characteristics and receive real-time predictions.

Wine quality prediction is an important task in the industry, as quality assessment is typically subjective and requires expert tasting. Machine learning helps automate this process using data-driven insights. ([Medium][1])

---

## 🎯 Objective

* Predict wine quality using machine learning
* Convert regression problem into classification (Good/Bad)
* Build and deploy a user-friendly web app
* Compare multiple ML models and optimize performance

---

## 📂 Dataset Description

The dataset contains chemical properties of wine, including:

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

🎯 **Target Variable:**

* `quality ≥ 7` → GOOD (1)
* `quality < 7` → BAD (0)

These physicochemical attributes play a key role in determining wine quality. ([GeeksforGeeks][2])

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit

---

## 🛠️ Project Workflow

### 1. Data Analysis

* Used `head()`, `info()`, `describe()`
* Checked missing values
* Visualized correlations

### 2. Data Preprocessing

* Created binary target (`quality_label`)
* Feature selection
* Train-test split

### 3. Model Training

Trained multiple models:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree

### 4. Feature Scaling

* Applied StandardScaler
* Compared performance before & after scaling

### 5. Model Comparison

* Evaluated using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score

### 6. Hyperparameter Tuning

* Used GridSearchCV
* Improved best model performance

### 7. Feature Importance

* Identified key features influencing wine quality

---

## 🚀 Deployment

The model is deployed using Streamlit:

👉 Users input wine properties
👉 Model processes data
👉 Predicts:

* GOOD 🍷
* BAD ❌

Streamlit allows quick deployment of ML models as interactive web apps without complex frontend development. ([anshg07.github.io][3])

---

## 🧠 How It Works

1. User enters wine parameters
2. Data is scaled using StandardScaler
3. Model predicts wine quality
4. Result is displayed with confidence

---

## 📁 Project Structure

```bash
│── app.py
│── wine_model.pkl
│── scaler.pkl
│── requirements.txt
│── project.ipynb
│── winequality.csv
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Results

* Compared multiple ML models
* Decision Tree / Best model selected
* Improved performance using scaling + tuning

---

## 📈 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Add visualization dashboard
* Support real-time dataset upload
* Improve UI/UX

---

## 🏁 Conclusion

This project demonstrates:

* Complete ML pipeline
* Model comparison & tuning
* Deployment using Streamlit

It shows how machine learning can be used for **real-world quality prediction systems**.

---

## 🙌 Author

**Jyothi Reddy M**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

[1]: https://medium.com/analytics-vidhya/wine-quality-prediction-app-8ba8291d40f9?utm_source=chatgpt.com "Wine Quality Prediction App Using Streamlit | by Stuti Singh | Analytics Vidhya | Medium"
[2]: https://www.geeksforgeeks.org/machine-learning/wine-quality-prediction-machine-learning/?utm_source=chatgpt.com "Wine Quality Prediction - Machine Learning - GeeksforGeeks"
[3]: https://anshg07.github.io/ansh/projects/wine.html?utm_source=chatgpt.com "Wine Quality Prediction with Streamlit App"
