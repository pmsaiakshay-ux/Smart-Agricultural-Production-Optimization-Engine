# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is a machine learning-powered web application that recommends the most suitable crop to grow based on agricultural conditions (Nitrogen, Phosphorous, Potassium, Temperature, Humidity, Soil pH, and Rainfall). By leveraging machine learning models, OptiCrop helps farmers and agricultural planners optimize crop yield and resources.

## Features
- **Machine Learning Pipeline**: Automates data preprocessing, scaling, training, evaluation, and selection of the best-performing classification model.
- **Support for 6 ML Algorithms**: Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Naive Bayes.
- **Dynamic Interactive Dashboard**: Modern dark/light theme web interface built with Bootstrap 5, featuring crop prediction, Confidence Scores, Suggested Fertilizers, and Farming Tips.
- **Farming Insights**: Features dynamic graphs for model accuracy comparison, feature importance, confusion matrix, and prediction history.
- **CSV Data Export**: Export prediction history to CSV format.
- **Dark Mode Support**: Toggle between dark and light themes dynamically.

---

## Folder Structure
```
OptiCrop/
├── app.py
├── requirements.txt
├── README.md
├── model/
│   ├── model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── dataset/
│   └── Crop_recommendation.csv
├── templates/
│   ├── index.html
│   ├── predict.html
│   ├── about.html
│   ├── result.html
│   └── layout.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── notebooks/
│   └── ML_Model.ipynb
└── utils/
    ├── train.py
    ├── preprocess.py
    ├── predict.py
    └── helper.py
```

---

## Installation & Setup

### Prerequisites
- Python 3.11+
- virtualenv (optional but recommended)

### 1. Setup Virtual Environment
First, clone or copy the project files to your workspace directory. Navigate to `OptiCrop/` and create a virtual environment:

```bash
# Using Python venv
python -m venv venv

# Activate Virtual Environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate Virtual Environment (Windows CMD)
.\venv\Scripts\activate.bat

# Activate Virtual Environment (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
Install all required libraries specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Dataset
The project uses the standard **Crop Recommendation Dataset** which contains 2,200 rows of soil and environmental parameters:
*   **N**: Nitrogen content ratio in soil
*   **P**: Phosphorous content ratio in soil
*   **K**: Potassium content ratio in soil
*   **temperature**: Temperature in Celsius
*   **humidity**: Relative humidity in percentage
*   **ph**: pH value of the soil
*   **rainfall**: Rainfall in mm
*   **label**: Output target crop (22 unique classes, such as rice, maize, coffee, etc.)

The dataset is automatically downloaded and saved to `dataset/Crop_recommendation.csv` when you run the training script.

---

## Training the ML Models
To train the models, compare their accuracies, select the best model, and save it to the `model/` folder:
```bash
python utils/train.py
```
This script will output:
- Train/Test accuracy for all 6 models.
- Confusion matrix and classification report.
- Features importance graph and model accuracy comparison chart (saved to static/images).
- `model/model.pkl`, `model/label_encoder.pkl`, and `model/scaler.pkl`.

---

## Running the Web Application
Start the local development server:
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Screenshots
*(Screenshots Placeholder - UI features standard responsive layouts, dark/light theme toggle, glassmorphism gradient containers, prediction input form with frontend validation, and dynamic visualization charts.)*

---

## Future Improvements
- **IoT Sensors Integration**: Connect real-time soil NPK and moisture sensors to feed inputs directly to the engine.
- **Location-Based Weather API Integration**: Fetch real-time weather forecasts (temperature, humidity, rainfall) automatically using geolocation.
- **Deep Learning Models**: Incorporate deep neural networks (MLPs) to compare performance against traditional classifiers.
- **Multilingual Support**: Add translations for regional languages to support farmers globally.
