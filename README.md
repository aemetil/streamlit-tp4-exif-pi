# TP4 - Streamlit : Édition des métadonnées EXIF d'une image

Ce projet a été réalisé dans le cadre du TP 4.2 du cours **Outils Collaboratifs**.  
Il s'agit d'une **application Streamlit** permettant de modifier les métadonnées EXIF d'une image JPEG.

---

## Fonctionnalités

- Import d'une image JPEG (ex : `mnemosyne.jpg`)
- Affichage de l’image sélectionnée
- Édition des métadonnées EXIF :
  - **Auteur** (`Artist`)
  - **Description de l’image** (`ImageDescription`)
  - **Coordonnées GPS** (Latitude, Longitude, format DMS)
- Sauvegarde de l’image avec les nouvelles métadonnées EXIF
- Bouton de téléchargement de l’image modifiée

---

## Déploiement

L’application est accessible en ligne via **Streamlit Community Cloud** à l’adresse suivante :  
👉 [Voir l'application en ligne](https://tp4-exif-gps.streamlit.app)

---

## Installation locale (optionnelle)

> Testée avec Python 3.11+

```bash
git clone https://github.com/aemetil/streamlit-tp4-exif-gps.git
cd streamlit-tp4-exif-gps
pip install -r requirements.txt
streamlit run app.py
```
