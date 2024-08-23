from django.shortcuts import render
from django.http import JsonResponse
import joblib
import numpy as np
import pandas as pd

# Load the model
model = joblib.load('../models/V2/naive_baye.pkl')

df1 = pd.read_csv('../data/Symptom-severity.csv')
df1['Symptom'] = df1['Symptom'].str.replace('_',' ')

discrp = pd.read_csv("../data/symptom_Description.csv")
ektra7at = pd.read_csv("../data/symptom_precaution.csv")

def predd(model, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17):
    psymptoms = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17]
    
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j] == a[k]:
                psymptoms[j] = b[k]
    
    psy = [psymptoms]
    
    pred2 = model.predict(psy)
    pred_proba = model.predict_proba(psy)[0]
    print(pred_proba)
    
    disease_name = pred2[0]
    description = discrp[discrp['Disease'] == disease_name].values[0][1]
    
    disease_index = np.where(model.classes_ == disease_name)[0][0]
    probability = pred_proba[disease_index] * 100 
    
    recommendations = ektra7at[ektra7at['Disease'] == disease_name]
    c = np.where(ektra7at['Disease'] == disease_name)[0][0]
    
    precautions = []
    for i in range(1, len(ektra7at.iloc[c])):
        precautions.append(ektra7at.iloc[c, i])
    
    result = {
        "disease_name": disease_name,
        "description": description,
        "precautions": precautions,
        "probability": round(probability, 2)
    }
    
    return result


def predict_disease(request):
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms', '').split(',')
        
        # Fill in the symptoms (up to 17)
        filled_symptoms = symptoms + [0] * (17 - len(symptoms))
        
        # Predict the disease and get the details
        result = predd(
            model, 
            *filled_symptoms
        )
        
        return JsonResponse(result)
    else:
        return render(request, 'predictor/predict.html')

def book_doctor(request):
    # Get the disease name from the request (from query parameters)
    disease_name = request.GET.get('disease_name', '')

    # Read the CSV files
    disease_specialist_df = pd.read_csv('../data/disease_specialist.csv')
    doctor_details_df = pd.read_csv('../data/doctor_description.csv')

    # Find the specialist for the given disease
    specialist_df = disease_specialist_df[disease_specialist_df['Disease'] == disease_name]
    if not specialist_df.empty:
        specialist = specialist_df['Specialist'].values[0]
    else:
        specialist = None
    
    print(specialist)

    # Filter doctors based on the specialist
    if specialist:
        doctors_df = doctor_details_df[doctor_details_df['Specialist'] == specialist]
    else:
        doctors_df = pd.DataFrame()  # Empty DataFrame if no specialist is found

    # Convert doctors DataFrame to a list of dictionaries
    doctors = doctors_df.to_dict(orient='records')
    print(doctors)

    # Pass the doctors and disease name to the template
    return render(request, 'predictor/book_doctor.html', {'doctors': doctors, 'disease_name': disease_name})