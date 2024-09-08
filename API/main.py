from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import numpy as np

#load model 
model1=pickle.load(open("model\Heart_prediction_Log.pkl",'rb'))

app=FastAPI()

class Input(BaseModel):
    Age:int
    Sex:int
    Chest_pain_type:int
    BP:int
    Colestrol:int
    FBS_over_120:int
    EKG_resuts:int
    Max_HR:int
    Exersice_anigna:int
    ST_depression:int
    Slope_of_ST:int
    No_of_vessels_fluro:int
    Thallium:int


@app.get("/")
def read_root():
    return {"msg":"Disease Predictor"}

@app.post("/predict")
def predict_disease(input:Input):
    data = input.model_dump()
    data_in=[[data['Age'],data['Sex'],data['Chest_pain_type'],data['BP'],data['Colestrol'],data['FBS_over_120'],data['EKG_resuts'],data['Max_HR'],data['Exersice_anigna'],data['ST_depression'],data['Slope_of_ST'],data['No_of_vessels_fluro'],data['Thallium'],]]

    prediction =list(model1.predict(data_in))
    return{
        'prediction':prediction[0]
    }

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)