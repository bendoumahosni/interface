#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests
import pandas as pd

# Streamlit App
st.title("Prédiction de classe pour un client")

# Zone de texte pour saisir le client_id
#client_id = st.text_input("Saisissez le client_id :", "")


df=pd.read_csv('test_app.csv')
list_clients=df['SK_ID_CURR']
client_id = st.selectbox(
    "selectionner le numero d'un client",
    (list_clients))

st.write('vous avez choisi:', client_id)

# Bouton pour effectuer la prédiction
if st.button("Effectuer la prédiction"):
   # Effectuer une requête GET à l'API FastAPI
    api_url = f"https://fethiza.onrender.com/predict/{client_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        prediction_result = response.json()
        st.success(f"Classe prédite pour le client {client_id} : {prediction_result['predicted_class']}")
        st.success(f"Score prédit pour le client {client_id} : {prediction_result['predicted_score']}")
    else:
            st.error(f"Erreur lors de la requête à l'API. Code d'erreur : {response.status_code}")
    

# In[ ]:




