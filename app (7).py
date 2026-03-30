
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('sal.pkl')

st.title('💰 Salary Predictor')

age = st.number_input('Age', 18, 65)
experience = st.number_input('Years of Experience', 0, 40)

if st.button('Predict Salary'):
    input_data = pd.DataFrame([[age, experience]],
                              columns=['Age', 'Years of Experience'])

    prediction = model.predict(input_data)
    st.success(f'💰 Predicted Salary: ₹{prediction[0]:,.2f}')
