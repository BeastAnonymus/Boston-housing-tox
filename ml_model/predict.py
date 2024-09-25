import joblib
import numpy as np
def predict(input_features):
    model = joblib.load('model.pkl')
# Predict and return result
    prediction = model.predict(np.array([input_features]))
    return prediction