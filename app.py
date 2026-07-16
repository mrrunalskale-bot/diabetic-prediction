import streamlit as st
import pickle as pkl

st.title('Diabetic Patient Prediction Project')
model = load(open('model.pkl','rb'))
scaler = load(open('scaler.pkl','rb'))

gender = st.selectbox('Enter gender',['male','female','other'])
if gender=='male':
    gender=0
elif gender=='female':
    gender=1
else:
    gender=2

age = st.number_input('Enter age',min_value=5,max_value=100)

hypertension = st.selectbox('Enter hypertension',['yes','no'])
if hypertension=='yes':
    hypertension=1
else:
    hypertension=0

heart_disease = st.selectbox('Enter heart_disease',['yes','no'])
if heart_disease=='yes':
    heart_disease=1
else:
    heart_disease=0

smoking_history = st.selectbox('Enetr smoking_history',['never', 'No Info', 'current', 'former', 'ever', 'not current'])
if smoking_history=='never':
    smoking_history=0
elif smoking_history=='No Info':
    smoking_history=1
elif smoking_history=='current':
    smoking_history=2
elif smoking_history=='former':
    smoking_history=3
elif smoking_history=='ever':
    smoking_history=2
else:
    smoking_history=-1

bmi = st.number_input('Enter bmi')

HbA1c_level = st.number_input('HbA1c_level')

blood_glucose_level = st.number_input('blood_glucose_level')

if st.button('Check'):
    result = model.predict(scaler.transform([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]]))
    result = result[0]
    if result == 1:
        st.error("Person is diabetic")
    else:
        st.success("Person is not diabetic")
