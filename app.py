import os
import json
import csv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from io import StringIO

# Add utils to python path dynamically
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from predict import predict_crop
from helper import get_crop_details

app = Flask(__name__)
app.secret_key = 'opti_crop_secret_key_for_flask'

# Simple file-based prediction history
HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'model', 'prediction_history.json')

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_history(entry):
    history = load_history()
    history.insert(0, entry)  # Add new prediction to the beginning
    # Keep last 50 predictions
    history = history[:50]
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve and validate inputs
        errors = {}
        try:
            n = float(request.form.get('n', '').strip())
            if n < 0 or n > 150:
                errors['n'] = 'Nitrogen (N) must be between 0 and 150 mg/kg.'
        except ValueError:
            errors['n'] = 'Please enter a valid number for Nitrogen.'

        try:
            p = float(request.form.get('p', '').strip())
            if p < 0 or p > 150:
                errors['p'] = 'Phosphorous (P) must be between 0 and 150 mg/kg.'
        except ValueError:
            errors['p'] = 'Please enter a valid number for Phosphorous.'

        try:
            k = float(request.form.get('k', '').strip())
            if k < 0 or k > 210:
                errors['k'] = 'Potassium (K) must be between 0 and 210 mg/kg.'
        except ValueError:
            errors['k'] = 'Please enter a valid number for Potassium.'

        try:
            temp = float(request.form.get('temp', '').strip())
            if temp < -10 or temp > 60:
                errors['temp'] = 'Temperature must be between -10°C and 60°C.'
        except ValueError:
            errors['temp'] = 'Please enter a valid number for Temperature.'

        try:
            humidity = float(request.form.get('humidity', '').strip())
            if humidity < 0 or humidity > 100:
                errors['humidity'] = 'Humidity must be between 0% and 100%.'
        except ValueError:
            errors['humidity'] = 'Please enter a valid number for Humidity.'

        try:
            ph = float(request.form.get('ph', '').strip())
            if ph < 0 or ph > 14:
                errors['ph'] = 'Soil pH must be between 0 and 14.'
        except ValueError:
            errors['ph'] = 'Please enter a valid number for Soil pH.'

        try:
            rainfall = float(request.form.get('rainfall', '').strip())
            if rainfall < 0 or rainfall > 500:
                errors['rainfall'] = 'Rainfall must be between 0 and 500 mm.'
        except ValueError:
            errors['rainfall'] = 'Please enter a valid number for Rainfall.'

        if errors:
            return render_template('predict.html', errors=errors, form_data=request.form)

        # Make prediction
        try:
            predicted_crop, confidence = predict_crop(n, p, k, temp, humidity, ph, rainfall)
            crop_details = get_crop_details(predicted_crop)
            
            # Format confidence
            conf_str = f"{confidence * 100:.2f}%" if confidence is not None else "N/A"
            
            # Save prediction history
            history_entry = {
                'n': n,
                'p': p,
                'k': k,
                'temp': temp,
                'humidity': humidity,
                'ph': ph,
                'rainfall': rainfall,
                'prediction': predicted_crop.capitalize(),
                'confidence': conf_str
            }
            save_history(history_entry)

            # Redirect to results page and pass arguments
            return render_template('result.html', 
                                   crop=predicted_crop.capitalize(),
                                   confidence=conf_str,
                                   fertilizer=crop_details['fertilizer'],
                                   conditions=crop_details['conditions'],
                                   tips=crop_details['tips'],
                                   inputs=history_entry)
        except FileNotFoundError:
            flash("Machine learning model files not found. Please train the model first by running 'python utils/train.py' in the backend terminal.", 'danger')
            return redirect(url_for('predict'))
        except Exception as e:
            flash(f"An error occurred during prediction: {e}", 'danger')
            return redirect(url_for('predict'))

    return render_template('predict.html', errors={}, form_data={})

@app.route('/history')
def history():
    return jsonify(load_history())

@app.route('/export')
def export_csv():
    history_data = load_history()
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Nitrogen', 'Phosphorous', 'Potassium', 'Temperature', 'Humidity', 'pH', 'Rainfall', 'Prediction', 'Confidence'])
    for row in history_data:
        cw.writerow([row['n'], row['p'], row['k'], row['temp'], row['humidity'], row['ph'], row['rainfall'], row['prediction'], row['confidence']])
    
    output = si.getvalue()
    return send_file(
        StringIO(output),
        mimetype="text/csv",
        as_attachment=True,
        download_name="prediction_history.csv"
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
