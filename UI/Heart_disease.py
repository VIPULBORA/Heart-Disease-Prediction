import streamlit as st
import requests
import json

def main():
    st.title("HEART DISEASE PRIDICTION")
    Age=st.number_input("Age")


    Sex = st.selectbox("Sex",("MALE","FEMALE"))
    if Sex=="MALE":
        Sex=1
    else:
        Sex=0

    Chest_pain_type=st.selectbox("Chest Pain Type",("Typical angina","Atypical angina","Non-anginal pain","asymptomatic"))
    if Chest_pain_type=="Typical angina":
        Chest_pain_type=1
    elif Chest_pain_type=="Atypical angina":
        Chest_pain_type=2
    elif Chest_pain_type=="Non-anginal pain":
        Chest_pain_type=3
    else:
        Chest_pain_type=4



    BP = st.number_input("Blood Pressure")

    if BP < 80 or BP > 200:
        st.warning("Blood Pressure should be between 80 and 200.")


        if st.button("Predict"):
            if 80 <= BP <= 200:
                BP=st.number_input("Blood Pressure")
                st.write("Proceeding with prediction...")
            else:
                st.error("Please enter a valid Blood Pressure value between 80 and 200.")



    

    Colestrol=st.number_input("Colestrol")

    FBS_over_120=st.selectbox("Fasting Blood Sugar",("Greater than 120 mg/dl","Less than 120mg/dl"))
    if FBS_over_120=="Greater than 120 mg/dl":
        FBS_over_120=1
    else:
        FBS_over_120=0
    
    EKG_resuts=st.selectbox("Resting Electrocardiographic Results",("Normal","Having ST-T wave abnormality","showing probable"))
    if EKG_resuts=="Normal":
        EKG_resuts=0
    elif EKG_resuts=="Having ST-T wave abnormality":
        EKG_resuts=1
    else:
        EKG_resuts=2

    Max_HR=st.number_input("Maximum Heart Rate")

    Exersice_anigna=st.selectbox("Exercise Induced Angina",("YES","NO"))
    if Exersice_anigna=="YES":
        Exersice_anigna=1
    else:
        Exersice_anigna=0

    ST_depression=st.number_input("ST depression induced by exercise relative to rest(0-10)")

    Slope_of_ST=st.selectbox("The Slope of the Peak exercise ST segment",("Upsloping","Flat","downsloping"))
    if Slope_of_ST=="Upsloping":
        Slope_of_ST=1
    elif Slope_of_ST=="Flat":
        Slope_of_ST=2
    else:
        Slope_of_ST=3

    No_of_vessels_fluro=st.selectbox("Number of Major vessels (0-3) Colored by Flourosopy",("1","2","3"))
    if No_of_vessels_fluro=="1":
        No_of_vessels_fluro=1
    elif No_of_vessels_fluro=="2":
        No_of_vessels_fluro=2
    else:
        No_of_vessels_fluro=3
    
    Thallium=st.selectbox("Thalium stress test result",("Normal","Fixed defect","reversable defect"))
    if Thallium=="Normal":
        Thallium=3
    elif Thallium=="Fixed defect":
        Thallium=6
    else:
        Thallium=7

    input_data={
        "Age":Age,
        "Sex":Sex,
        "Chest_pain_type":Chest_pain_type,
        "BP":BP,
        "Colestrol":Colestrol,
        "FBS_over_120":FBS_over_120,
        "EKG_resuts":EKG_resuts,
        "Max_HR":Max_HR,
        "Exersice_anigna":Exersice_anigna,
        "ST_depression":ST_depression,
        "Slope_of_ST":Slope_of_ST,
        "No_of_vessels_fluro":No_of_vessels_fluro,
        "Thallium":Thallium,
    }

    predict="Absent"
    if st.button("Predict"):
        predict=requests.post(url="http://127.0.0.1:8000/predict",data=json.dumps(input_data))
        predict=predict.json()
        p=predict['prediction']
        st.success(f'{p}')

if __name__=='__main__':
    main()


