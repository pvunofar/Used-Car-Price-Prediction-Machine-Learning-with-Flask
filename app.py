from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import joblib
import pandas as pd

path = 'C:/Users/PHUOC/Downloads/DuDoanGiaXeCu/randomforest_model.pkl'
rd_model = joblib.load(path)

app = Flask(__name__)
app.secret_key = 'cs466g'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def getInput():
    predict_value_to_float = None 

    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            km_driven = int(request.form['km_driven'])
            fuel = int(request.form['fuel'])
            seller_type = int(request.form['seller_type'])
            transmission = int(request.form['transmission'])
            owner = int(request.form['owner'])
            mileage = float(request.form['mileage'])
            engine = float(request.form['engine'])
            max_power = float(request.form['max_power'])
            seats = float(request.form['seats'])

            input_data = pd.DataFrame([[year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
                                      columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats'])
            
            predict_value = rd_model.predict(input_data)
            # Chuyển đổi INR sang USD
            predict_value_to_float = (float(predict_value)) * 0.01178

        except Exception as e:
            flash(f"Error: {e}")  

    return render_template('index.html', display=predict_value_to_float)

if __name__ == '__main__':
    app.run(debug=True)

