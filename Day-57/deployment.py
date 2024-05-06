import streamlit as st
from helpers import get_save_file
import numpy as np

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

if __name__ == "__main__":
    st.title("Hello Everyone !")

    sl = st.number_input("Enter Sepal Length")
    sw = st.number_input("Enter Sepal Width")
    pl = st.number_input("Enter Petal Length")
    pw = st.number_input("Enter Petal Width")

    user_input = np.array([[sl, sw, pl, pw]])
    
    if st.button("Predict"):
        st.write(
            f"Given flower is of {prediction(user_input)} type !\nThank you !"
        )