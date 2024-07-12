#1 IMPORTATION DES LIBRAIRIES
#2 DESCRIPTION DU POJET
#3 CHARGEMENT DU MODELE
#4 DEFINITION DE LA FONCTION D'INTERFERENCE(PERMET DE FAIRE LA PREDICTION)
#5 SAISIE DES INFORMATIONS
#6CREATION DU BOUTON DE PREDICTION


#1 imporation des librairies
import streamlit as st
import numpy as np
import joblib 

#2 DESCRIPTION DU PROJET

st.title("PREDICTION DE DESABONNEMENT DES CLIENTS DE EXPRESSO")

#3 CHARGEMENT DU MODELE
@st.cache_data(persist=True)
def load_model ():
    data = joblib.load('datasets_db/model_expresso.joblib')

    return data

expres_mod = load_model()

#4 DEFINITION DE LA FONCTION D'INTERFERENCE 

def interference(REGULARITY,REVENUE,MONTANT,ON_NET,ARPU_SEGMENT,DATA_VOLUME,FREQUENCE,FREQUENCE_RECH,ORANGE):
    
    df = np.array([REGULARITY,REVENUE,MONTANT,ON_NET,ARPU_SEGMENT,DATA_VOLUME,FREQUENCE,FREQUENCE_RECH,ORANGE])
    
    pred = expres_mod.predict(df.reshape(1,-1))
    return pred

#5 SAISIE DES INFORMATIONS DU CLIENT
st.write('Entrez les informations du client')

REGULARITY = st.number_input(label='Donner la regularité', min_value=1.0, value=8.0)

REVENUE = st.number_input(label='Donner le montant du revenu', min_value=1.0, value=3000.0)

MONTANT = st.number_input(label='Donner le montant', min_value=10.0, value=3000.0)

ON_NET  = st.number_input(label='Donner le ON_NET', min_value=0.0, value=27.0)

ARPU_SEGMENT = st.number_input(label='Donner la ARPU segment', min_value=0.0, value=1000.0)

DATA_VOLUME = st.number_input(label='Donner le volume de data', min_value=0.0, value=257.0)

FREQUENCE = st.number_input(label='Donner la fréquence', min_value=1.0, value=9.0)

FREQUENCE_RECH = st.number_input(label='Niveau de fréquence de la recherche', min_value=1.0, value=7.0)

ORANGE = st.number_input(label="Nombre d'appel à orange", min_value=0.0, value=29.0)

# FREQ_TOP_PACK = st.number_input(label='Donner la fréquence de souscription')
# REGION7 =  st.number_input(label='Donner le numero de la region',min_value = 0,max_value =1  )
# TENURE4 = st.number_input(label='Donner le numero de la tenure',min_value = 0,max_value =1)
# TOP_PACK50 = st.number_input(label='Donner la premiere souscription',min_value = 0,max_value =2)

#6 CREATION DU BOUTON DE PREDICTION

if st.button('predict'):
    result_pred = interference(REGULARITY,REVENUE,MONTANT,ON_NET,ARPU_SEGMENT,DATA_VOLUME,FREQUENCE,FREQUENCE_RECH,ORANGE)
    if result_pred[0]==0:
        st.success("Le client est abonné")
    elif result_pred[0]==1:
        st.warning("Le client est désabonné")
    





 
