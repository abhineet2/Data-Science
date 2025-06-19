import pickle
import streamlit as st
from streamlit_option_menu import option_menu

dia_model = pickle.load(open("./Predictions/diabetes.sav", 'rb'))
heart_model = pickle.load(open("./Predictions/Heart.sav",'rb'))
par_model = pickle.load(open("./Predictions/Parkinson.sav",'rb'))

with st.sidebar:
    selected = option_menu("Disease Prediction System",
                           ["Diabetes Prediction",
                            "Heart Disease Prediction",
                            "Parkinson's Prediction"],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        Glucose = st.text_input("Glucose Level")
        BloodPressure = st.text_input("Blood Pressure Value")
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")
        BMI = st.text_input("BMI Value")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
        Age = st.text_input("Age")

        result_dia = ""

    if st.button("Predict"):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        input_data = [float(i) for i in input_data]
        prediction = dia_model.predict([input_data])
        if prediction[0] == 0:
            result_dia = "The person is not diabetic."
        else:
            result_dia = "The person is diabetic."
    st.success(result_dia)

elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input("Age")
        sex = st.text_input("Sex")
        cp = st.text_input("Chest Pain Type (0-3)")
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol")
        fbs = st.text_input("Fasting Blood Sugar (0 or 1)")
        restecg = st.text_input("Resting Electrocardiographic Results (0-2)")
        thalach = st.text_input("Maximum Heart Rate Achieved")
        exang = st.text_input("Exercise Induced Angina (0 or 1)")
        oldpeak = st.text_input("Oldpeak")
        slope = st.text_input("Slope of the Peak Exercise ST Segment (0-2)")    
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy (0-3)")
        thal = st.text_input("Thalassemia (0-3)")
    
    result_heart = ""
    if st.button("Predict"):
        input_data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        input_data = [float(i) for i in input_data]
        prediction = heart_model.predict([input_data])
        if prediction[0] == 0:
            result_heart = "The person does not have heart disease."
        else:
            result_heart = "The person has heart disease."
    st.success(result_heart)

elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Prediction")
    col1, col2,col3,col4,col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        fhi = st.text_input("MDVP:Fhi(Hz)")
        flo = st.text_input("MDVP:Flo(Hz)")
    with col2:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        RAP = st.text_input("MDVP:RAP")
    with col3:
        PPQ = st.text_input("MDVP:PPQ")
        DDP = st.text_input("Jitter:DDP")
        Shimmer = st.text_input("MDVP:Shimmer")
    with col4:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        APQ3 = st.text_input("Shimmer:APQ3")
        APQ5 = st.text_input("Shimmer:APQ5")
    with col5:
        APQ = st.text_input("MDVP:APQ")
        DDA = st.text_input("Shimmer:DDA")
        NHR = st.text_input("NHR")
        HNR = st.text_input("HNR")
        RPDE = st.text_input("RPDE")
        DFA = st.text_input("DFA")
        spread1 = st.text_input("spread1")
        spread2 = st.text_input("spread2")
        D2 = st.text_input("D2")
        PPE = st.text_input("PPE")
    result_par = ""
    if st.button("Predict"):
        input_data = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        input_data = [float(i) for i in input_data]
        prediction = par_model.predict([input_data])
        if prediction[0] == 0:
            result_par = "The person does not have Parkinson's disease."
        else:
            result_par = "The person has Parkinson's disease."
    st.success(result_par)

