# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:17:38 2023

@author: abc
"""
import numpy as np
import pickle
import streamlit as st
import requests
from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd

dec_tree=pickle.load(open('D:/practice/Firebase/decision_model.sav', 'rb'))

symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze']




symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index
 
data_dict = {'symptom_index': {'itching': 0,
  'skin_rash': 1,
  'nodal_skin_eruptions': 2,
  'continuous_sneezing': 3,
  'shivering': 4,
  'chills': 5,
  'joint_pain': 6,
  'stomach_pain': 7,
  'acidity': 8,
  'ulcers_on_tongue': 9,
  'muscle_wasting': 10,
  'vomiting': 11,
  'burning_micturition': 12,
  'spotting_ urination': 13,
  'fatigue': 14,
  'weight_gain': 15,
  'anxiety': 16,
  'cold_hands_and_feets': 17,
  'mood_swings': 18,
  'weight_loss': 19,
  'restlessness': 20,
  'lethargy': 21,
  'patches_in_throat': 22,
  'irregular_sugar_level': 23,
  'cough': 24,
  'high_fever': 25,
  'sunken_eyes': 26,
  'breathlessness': 27,
  'sweating': 28,
  'dehydration': 29,
  'indigestion': 30,
  'headache': 31,
  'yellowish_skin': 32,
  'dark_urine': 33,
  'nausea': 34,
  'loss_of_appetite': 35,
  'pain_behind_the_eyes': 36,
  'back_pain': 37,
  'constipation': 38,
  'abdominal_pain': 39,
  'diarrhoea': 40,
  'mild_fever': 41,
  'yellow_urine': 42,
  'yellowing_of_eyes': 43,
  'acute_liver_failure': 44,
  'fluid_overload': 45,
  'swelling_of_stomach': 46,
  'swelled_lymph_nodes': 47,
  'malaise': 48,
  'blurred_and_distorted_vision': 49,
  'phlegm': 50,
  'throat_irritation': 51,
  'redness_of_eyes': 52,
  'sinus_pressure': 53,
  'runny_nose': 54,
  'congestion': 55,
  'chest_pain': 56,
  'weakness_in_limbs': 57,
  'fast_heart_rate': 58,
  'pain_during_bowel_movements': 59,
  'pain_in_anal_region': 60,
  'bloody_stool': 61,
  'irritation_in_anus': 62,
  'neck_pain': 63,
  'dizziness': 64,
  'cramps': 65,
  'bruising': 66,
  'obesity': 67,
  'swollen_legs': 68,
  'swollen_blood_vessels': 69,
  'puffy_face_and_eyes': 70,
  'enlarged_thyroid': 71,
  'brittle_nails': 72,
  'swollen_extremeties': 73,
  'excessive_hunger': 74,
  'extra_marital_contacts': 75,
  'drying_and_tingling_lips': 76,
  'slurred_speech': 77,
  'knee_pain': 78,
  'hip_joint_pain': 79,
  'muscle_weakness': 80,
  'stiff_neck': 81,
  'swelling_joints': 82,
  'movement_stiffness': 83,
  'spinning_movements': 84,
  'loss_of_balance': 85,
  'unsteadiness': 86,
  'weakness_of_one_body_side': 87,
  'loss_of_smell': 88,
  'bladder_discomfort': 89,
  'foul_smell_of urine': 90,
  'continuous_feel_of_urine': 91,
  'passage_of_gases': 92,
  'internal_itching': 93,
  'toxic_look_(typhos)': 94,
  'depression': 95,
  'irritability': 96,
  'muscle_pain': 97,
  'altered_sensorium': 98,
  'red_spots_over_body': 99,
  'belly_pain': 100,
  'abnormal_menstruation': 101,
  'dischromic _patches': 102,
  'watering_from_eyes': 103,
  'increased_appetite': 104,
  'polyuria': 105,
  'family_history': 106,
  'mucoid_sputum': 107,
  'rusty_sputum': 108,
  'lack_of_concentration': 109,
  'visual_disturbances': 110,
  'receiving_blood_transfusion': 111,
  'receiving_unsterile_injections': 112,
  'coma': 113,
  'stomach_bleeding': 114,
  'distention_of_abdomen': 115,
  'history_of_alcohol_consumption': 116,
  'fluid_overload.1': 117,
  'blood_in_sputum': 118,
  'prominent_veins_on_calf': 119,
  'palpitations': 120,
  'painful_walking': 121,
  'pus_filled_pimples': 122,
  'blackheads': 123,
  'scurring': 124,
  'skin_peeling': 125,
  'silver_like_dusting': 126,
  'small_dents_in_nails': 127,
  'inflammatory_nails': 128,
  'blister': 129,
  'red_sore_around_nose': 130,
  'yellow_crust_ooze': 131},
 'predictions_classes':['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne',
        'Alcoholic hepatitis', 'Allergy', 'Arthritis', 'Bronchial Asthma',
        'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis',
        'Common Cold', 'Dengue', 'Diabetes ',
        'Dimorphic hemmorhoids(piles)', 'Drug Reaction',
        'Fungal infection', 'GERD', 'Gastroenteritis', 'Heart attack',
        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
        'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia',
        'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
        'Osteoarthristis', 'Paralysis (brain hemorrhage)',
        'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Tuberculosis',
        'Typhoid', 'Urinary tract infection', 'Varicose veins',
        'hepatitis A']}

def inputd(symptoms):
    symptoms = symptoms.split(",")
     
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
         
    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)
    return input_data





MAPBOX_API_KEY = "sk.eyJ1IjoiaXNoYWFuMTMxMyIsImEiOiJjbGhoY21yMzQyZWh0M2ZudWdlMnk5cHE1In0.xfIE3yTkzMCvXyCP_DTDCg"

# Geocoding function to obtain latitude and longitude
def geocode_location(location):
    geolocator = Nominatim(user_agent="hospital-finder")
    location_data = geolocator.geocode(location)
    return location_data.latitude, location_data.longitude

# Function to fetch hospital data near the given coordinates
def fetch_hospitals(latitude, longitude):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/hospital.json?proximity={longitude},{latitude}&access_token={MAPBOX_API_KEY}"
    response = requests.get(url)
    data = response.json()
    hospitals = data.get("features", [])
    return hospitals

# Main Streamlit app code

    

def main():
    
    
    # giving a title
    st.title('Prediction Web App')
    
    
    # getting the input data from the user
    symp1 = st.selectbox(
    'Enter first symptom',
    ('itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze'))

    st.write('You selected:', symp1)
    
    symp2 = st.selectbox(
    'Enter Second symptom',
    ('itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze'))

    st.write('You selected:', symp2)
    
    symp3 = st.selectbox(
    'Enter Third symptom',
    ('itching', 'skin_rash', 'nodal_skin_eruptions',
       'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
       'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
       'vomiting', 'burning_micturition', 'spotting_ urination',
       'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets',
       'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
       'patches_in_throat', 'irregular_sugar_level', 'cough',
       'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
       'dehydration', 'indigestion', 'headache', 'yellowish_skin',
       'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
       'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea',
       'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
       'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
       'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision',
       'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
       'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
       'fast_heart_rate', 'pain_during_bowel_movements',
       'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus',
       'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
       'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
       'excessive_hunger', 'extra_marital_contacts',
       'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',
       'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
       'swelling_joints', 'movement_stiffness', 'spinning_movements',
       'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
       'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
       'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
       'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain',
       'altered_sensorium', 'red_spots_over_body', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches',
       'watering_from_eyes', 'increased_appetite', 'polyuria',
       'family_history', 'mucoid_sputum', 'rusty_sputum',
       'lack_of_concentration', 'visual_disturbances',
       'receiving_blood_transfusion', 'receiving_unsterile_injections',
       'coma', 'stomach_bleeding', 'distention_of_abdomen',
       'history_of_alcohol_consumption', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
       'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
       'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
       'inflammatory_nails', 'blister', 'red_sore_around_nose',
       'yellow_crust_ooze'))

    st.write('You selected:', symp3)
    
    
    # code for Prediction
    diagnosis = ''
    #diagnosis2=''
    # creating a button for Prediction
    if st.button('Prediction Result'):
        str=symp1+","+symp2+","+symp3
        inputdata=inputd(str)
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(inputdata)
        
        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        diagnosis = data_dict["predictions_classes"][dec_tree.predict(input_data_reshaped)[0]]
       
    st.success(diagnosis)
    

    # Get user location
    location = st.text_input("Enter your location:")
    if not location:
        st.warning("Please enter a location.")
        return

    # Obtain latitude and longitude
    try:
        latitude, longitude = geocode_location(location)
    except:
        st.error("Error occurred while geocoding. Please try again.")
        return

    # Fetch hospitals near the given location
    hospitals = fetch_hospitals(latitude, longitude)

    # Display hospital information
    if not hospitals:
        st.warning("No hospitals found near your location.")
    else:
        st.success(f"Found {len(hospitals)} hospitals near your location.")

        # Prepare the hospital data for mapping
        hospital_data = []
        for hospital in hospitals:
            name = hospital.get("text", "")
            hospital_center = hospital.get("center", [])
            if len(hospital_center) == 2:
                hospital_data.append({"name": name, "latitude": hospital_center[1], "longitude": hospital_center[0]})

        # Display the map centered at the specified location
        if hospital_data:
            df = pd.DataFrame(hospital_data)
            st.map(df)

        for hospital in hospital_data:
            name = hospital["name"]
            address = ", ".join(hospital.get("place_name", "").split(",")[:-2])
            distance_to_hospital = distance.distance((latitude, longitude), (hospital["latitude"], hospital["longitude"])).kilometers
            st.write(f"- {name}")
            st.write(f"  Address: {address}")
            st.write(f"  Distance: {distance_to_hospital:.2f} km")
  



    
    
if __name__ == '__main__':
    main()