import pandas as pa
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from decouple import config
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def creat_ai():
    try:
        status = True
        ENGINE = config('ENGINE')
        engine = create_engine(ENGINE)
        
        query = "SELECT name, year, mileage, transmission, fuel, body_status, price FROM car;"
        fd = pa.read_sql(query, engine)
        
        label_encoders = {}
        for column in ['name', 'transmission', 'fuel', 'body_status']:
            le = LabelEncoder()
            fd[column] = le.fit_transform(fd[column])
            label_encoders[column] = le
        
        x = fd[['year', 'mileage', 'name', 'transmission', 'fuel', 'body_status']]
        y = fd['price']
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        print(f"MAE: {mae}")
        print(f"MSE: {mse}")
        print(f"RMSE: {rmse}")
        print(f"R²: {r2}")
        return status, label_encoders, model
    except Exception:
        return False, None, None
def predict_price(car_name, car_year, car_mileage, car_transmission, car_fuel, car_body_status, label_encoders, model):
    if car_name not in label_encoders['name'].classes_:
        print(f"Warning: The car name '{car_name}' is not recognized.")
        return None

    car_name_encoded = label_encoders['name'].transform([car_name])[0]
    car_transmission_encoded = label_encoders['transmission'].transform([car_transmission])[0]
    car_fuel_encoded = label_encoders['fuel'].transform([car_fuel])[0]
    car_body_status_encoded = label_encoders['body_status'].transform([car_body_status])[0]

    input_data = pa.DataFrame([[car_year, car_mileage, car_name_encoded, car_transmission_encoded, car_fuel_encoded,car_body_status_encoded]],columns=['year', 'mileage', 'name', 'transmission', 'fuel', 'body_status'])
    predicted_price = model.predict(input_data)
    return predicted_price[0]

