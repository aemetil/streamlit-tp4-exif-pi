import streamlit as st
import datetime

# Titre
st.set_page_config(page_title="Ma date dans PI", layout="centered")
st.title("Votre date de naissance se cache-t-elle dans PI?")

# lecture des décimales de PI
@st.cache_data
def charger_pi():
    try:
        with open("pi_million_digits.txt", "r") as f:
            pi = f.read().replace("\n", "").replace(" ", "") # remplacer retour à la ligne & espaces
            if pi.startswith("3."):
                pi = pi[2:] #supprimer le "3." du debut
            return pi
    except FileNotFoundError:
        st.error("Le fichier pi_million_digits.txt est introuvable.")
        return ""

pi_million_digits = charger_pi()

# saisie de la date
date_naissance = st.text_input("Entrez votre date de naissance (format JJMMAAAA) :", max_chars=8)

# vérification
if date_naissance:
    if not date_naissance.isdigit() or len(date_naissance) != 8:
        st.warning("Veuillez saisir la date au format JJMMAAAA (ex : 01012000).")
    else:
        if date_naissance in pi_million_digits:
            position = pi_million_digits.index(date_naissance)
            st.success(f"Votre date apparaît dans PI à la position {position}!")
        else:
            st.info("Votre date ne figure pas dans le premier million de décimales de PI.")


#************ CONSIGNE 2 *******************
if len(date_naissance) == 8 and date_naissance.isdigit():
    # formater date_naissance au format attendu par strftime : JJ/MM/AAAA
    date_formatee = f"{date_naissance[:2]}/{date_naissance[2:4]}/{date_naissance[4:]}"
    date_naiss = datetime.datetime.strptime(date_formatee, "%d/%m/%Y").date()
    jour_semaine = date_naiss.strftime("%A")
    
    # dico pour la treduction des jours
    jour_fr = {
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", "Tuesday": "Jeudi",
        "Friday": "Vendredi", "Saturday": "Samedi", "Sunday":"Dimanche"
    }
    
    st.success(f"Vous êtes né(e) un {jour_fr[jour_semaine]}")
#else:
   # st.info("Format invalide. Veuillez entrer une date au format JJMMAAAA")
    
    
#******** CONSIGNE 3 *************
st.subheader("Calculs sur le premier million de decimales de PI")

pi_digits = charger_pi()

if pi_digits:
    # somme des 20 prémières décimales
    somme_20 = sum(int(i) for i in pi_digits[:20])
    
    # Somme des 12^2 = 144 premieres decimales
    somme_144 = sum(int(k) for k in pi_digits[:144])
    
    st.write(f"Somme des 20 premières décimales de PI : **{somme_20}**")
    st.write(f"Somme des 144 premières décimales de PI : **{somme_144}**")
    
    st.text_area("Que remarquez-vous?", placeholder="Écrivez ici votre observation...")
    
#************ CONSIGNE 4 ************

#intégrer une vidéo
st.subheader("L'incroyable addition : 1 + 2 + 3 + 4 +... = -1/12")
st.video("https://www.youtube.com/watch?v=xqTWRtNDO3U")
