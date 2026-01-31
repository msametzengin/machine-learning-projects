# Heart Attack Risk Prediction

This project aims to predict heart disease (heart attack) risk using real-world medical data and basic machine learning techniques.
A simple Artificial Neural Network (ANN) model is trained after data preprocessing, class balancing with SMOTE, and feature scaling.
In addition, its accuracy rate was compared with other models (Random Forest, Decision Tree, Logistic Regression).
The project also allows users to enter their own data via the terminal and receive a risk prediction.

---

## Proje Açıklaması:

Bu proje, gerçek tıbbi veriler kullanılarak yapay zeka (makine öğrenmesi) yöntemleri ile **kalp hastalığı (kalp krizi) riski tahmini** yapmayı amaçlamaktadır.
Veri ön işleme, sınıf dengesizliğini gidermek için **SMOTE**, ölçeklendirme ve basit bir **Yapay Sinir Ağı (ANN)** modeli kullanılmıştır.
Ayrıca, diğer modeller ile doğruluk oranı karşılaştırılmıştır. (Random Forest, Decision Tree, Logistic Regression)
Ayrıca kullanıcıdan terminal üzerinden veri alarak tahmin yapılabilmektedir.

---

## 📊 Dataset / Veri Seti

**Heart Failure Prediction Dataset**

- Source / Kaynak:  
  https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

This dataset is publicly available and is used for educational purposes only.
(Bu veri seti herkese açık olup yalnızca eğitim ve analiz amaçlı kullanılmıştır.)

---

## 🛠️ Technologies / Kullanılan Teknolojiler

- Python (3.10.11)
- NumPy & Pandas  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- TensorFlow / Keras
- Matplotlib

---

## 🚀 How It Works / Nasıl Çalışır?

1. Dataset is loaded and preprocessed (1. Veri seti yüklenir ve ön işleme tabi tutulur.)
2. Categorical features are encoded (2. Kategorik özellikler kodlanır.)
3. Data is split into training and testing sets (3. Veriler eğitim ve test setlerine ayrılır.)
4. Class imbalance is handled using SMOTE (4. SMOTE kullanılarak sınıf dengesizliği giderilir.)
5. Features are scaled using StandardScaler (5. Özellikler StandardScaler kullanılarak ölçeklendirilir.)
6. ANN model is trained (6. Yapay sinir ağı modeli eğitilir.)
7. User inputs are taken from the terminal for prediction (7. Tahmin için terminalden kullanıcı girdileri alınır.)

---

## ▶️ Usage / Kullanım

Install required libraries:

```bash
pip install -r requirements.txt
