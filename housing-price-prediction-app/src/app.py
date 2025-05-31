from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('src/model/housing_price_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    furnishingstatus_encoded = int(request.form['furnishingstatus_encoded'])
    airconditioning_encoded = int(request.form['airconditioning_encoded'])

    features = np.array([[area, bedrooms, bathrooms, furnishingstatus_encoded, airconditioning_encoded]])
    predicted_price = model.predict(features)

    return render_template('index.html', predicted_price=predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)