# Housing Price Prediction App

This project is a web application that predicts housing prices based on user input features. It utilizes a machine learning model saved in a Joblib file and is built using Flask.

## Project Structure

```
housing-price-prediction-app
├── src
│   ├── app.py                # Main application file
│   ├── model
│   │   └── housing_price_model.joblib  # Saved machine learning model
│   └── templates
│       └── index.html        # HTML template for user interface
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Requirements

To run this application, you need to have Python installed along with the required libraries. You can install the necessary libraries using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:
   ```
   cd housing-price-prediction-app
   ```

2. Run the application:
   ```
   python src/app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Input the required housing features in the form provided on the web interface.
- Click the submit button to get the predicted housing price based on the input features.

## License

This project is licensed under the MIT License.