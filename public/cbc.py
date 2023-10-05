# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:49:50 2023

@author: abc
"""
import numpy as np
import pandas as pd
import streamlit as st

def main():
    st.title('Disease prediction Web App by report analysis')
    
    rbc = st.text_input('Enter count of rbc in million/cu mm')
    
    if st.button('Check RBC'):
        rbc_value = float(rbc)  # Convert input to float
        
        if rbc_value > 7:
            st.success('Symptoms of polycythemia')
        elif 4 <= rbc_value <= 5.5:  # Use logical "and" instead of "&&"
            st.success('Normal')
        else:
            st.success('Symptoms of anaemia')
            
            
    hb = st.text_input('Enter value of hemoglobin in gm/dl')
    
    if st.button('Check HB'):
        hbc_value = float(hb)  # Convert input to float
        
        if 12 <= hbc_value <= 16:  # Use logical "and" instead of "&&"
            st.success('Normal')
        else:
            st.success('Symptom from anaemia')      
            
            
            
            
    mcv = st.text_input('Enter value of Mean corpuscular volume(MCV) in fl')
    
    if st.button('Check MCV'):
        mcv_value = float(mcv)  # Convert input to float
        
        if 78 <= mcv_value <= 90:  # Use logical "and" instead of "&&"
            st.success('Normal')
        elif 90 <= mcv_value:  # Use logical "and" instead of "&&"
             st.success('Symptom of B12 deficiency')    
        else:
            st.success('Symptom from iron deficiency')  
            
            
            
            
    mhc = st.text_input('Enter value of Mean corpuscular hemoglobin(MCH) in pg')
    
    if st.button('Check MCH'):
        mhc_value = float(mhc)  # Convert input to float
        
        if 27 <= mhc_value <= 32:  # Use logical "and" instead of "&&"
            st.success('Normal')
        else:
            st.success('Symptom from anaemia')  
            
            
            
            
    mchc = st.text_input('Enter value of Mean corpuscular hemoglobin concentration (MCHC)')
    
    if st.button('Check MCHC'):
        mchc_value = float(mchc)  # Convert input to float
        
        if 30 <= mchc_value <= 38:  # Use logical "and" instead of "&&"
            st.success('Normal')
        else:
            st.success('Symptom from anaemia')  
            
            
            
    wbc = st.text_input('Enter value of White blood cell in/cumm')
    
    if st.button('Check WBC'):
        wbc_value = float(wbc)  # Convert input to float
        
        if 4000 <= wbc_value <= 11000:  # Use logical "and" instead of "&&"
            st.success('Normal')
        elif wbc_value <= 4000:  # Use logical "and" instead of "&&"
             st.success('Symptom of viral infection, malaria, dengue , typhoid etc.')    
        else:
            st.success('Symptom of bacterial infection, pneumonia, urinary tract infection')  
            
            
            
    nb = st.text_input('Enter value of neutrophil')
    
    if st.button('Check Neutophil'):
        nbc_value = float(nb)  # Convert input to float
        
        if 50 <= nbc_value <= 70:  # Use logical "and" instead of "&&"
            st.success('Normal')
        elif nbc_value <= 50:  # Use logical "and" instead of "&&"
             st.success('Symptom of tuberclosis, bone marrow failure, auto immune disease , typhoid ')    
        else:
            st.success('Symptom of bacterial infection, acute infection')  
            
            
            
    lc = st.text_input('Enter value of Lymphocyte')
    
    if st.button('Check Lymphocyte'):
        lc_value = float(lc)  # Convert input to float
        
        if 20 <= lc_value <= 30:  # Use logical "and" instead of "&&"
            st.success('Normal')
        elif lc_value <= 20:  # Use logical "and" instead of "&&"
             st.success('Symptom of Cancer, AIDS')    
        else:
            st.success('Symptom of tuberclosis, thyroid, malnutrition, mumps')  
            
            
            
    eb = st.text_input('Enter value of Eosinophil')
    
    if st.button('Check Eosinophil'):
        ebc_value = float(eb)  # Convert input to float
        
        if 0 <= ebc_value <= 4:  # Use logical "and" instead of "&&"
            st.success('Normal')
        else:
            st.success('Symptom from allergy, blood parasite, intestinal parasite')     
            
            
            
    pl = st.text_input('Enter value of Platelets in /cumm')
    
    if st.button('Check Platelets'):
        plc_value = float(pl)  # Convert input to float
        
        if 150000 <= plc_value <= 450000:  # Use logical "and" instead of "&&"
            st.success('Normal')
        elif plc_value <= 150000:  # Use logical "and" instead of "&&"
             st.success('Symptom of viral infection, malaria, dengue , typhoid, small pox, chicken pox')    
        else:
            st.success('Symptom of Haemorrhage, fracture, injury, after operation')  
            
            
            
            
    tlc = st.text_input('Enter value of Total leucocyte count in /ul of blood ')
    
    if st.button('Check TLC'):
        tlc_value = float(tlc)  # Convert input to float
    
        if 4000 <= tlc_value <= 11000:  # Use logical "and" instead of "&&"
            st.success('Normal') 
        else:
            st.success('Symptom of leucopenia')  
            
            
            
     
            
     
            
            
            
            
            

if __name__ == '__main__':
    main()
