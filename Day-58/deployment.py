import fastapi
from helpers import get_save_file
import numpy as np

app = fastapi.FastAPI(title="Machine Learning - Iris dataset")

LABELS = {
    0: 'Iris-setosa',
    1 : 'Iris-versicolor', 
    2 : 'Iris-virginica'
}
best_scaler = get_save_file("best_model/standard_scaler.pkl")
best_model = get_save_file("best_model/reg_logistic_model.pkl")

def prediction(user_input):
    model_output = best_model.predict(
        best_scaler.transform(
            user_input
        )
    )[0]
    return LABELS[model_output]

@app.post("/predict")
def web_prediction(user_input):
    user_input = np.array([eval(user_input)])
    model_output = prediction(user_input)
    
    return {
        'status': "success",
        'result':model_output
    }


