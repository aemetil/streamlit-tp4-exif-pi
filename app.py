import streamlit as st

st.set_page_config(page_title="TP4 - Accueil", layout="centered")
st.title("TP4 - Outils Collaboratifs")
st.write("Bienvenue dans mon application Streamlit multiplage.")

st.sidebar.success("Selectionnez un TP dans le menu.")

st.markdown("""
### 📸 TP4.2 — Édition des métadonnées EXIF  
Modifiez et affichez les métadonnées EXIF (auteur, description, coordonnées GPS) et visualisez les lieux sur une carte.

---

### 🔎 TP4.3 — Recherche dans les décimales de PI  
Recherchez votre date de naissance dans le million de décimales de PI !
""")