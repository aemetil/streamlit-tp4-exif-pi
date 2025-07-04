# TP4 - Streamlit : Édition des métadonnées EXIF d'une image

Ce projet a été réalisé dans le cadre du TP 4.2 du cours **Outils Collaboratifs**.  
Il s'agit d'une **application Streamlit** permettant de:

- Modifier les métadonnées EXIF d'une image JPEG
- Ajouter ou modifier les coordonnées GPS d'une image
- Visualiser l'image et sa geolocalisation sur une carte
- Afficher des lieux visités ou rêvés sur une carte interactive

---

## Fonctionnalités

- **Import** d'une image JPEG (ex : `mnemosyne.jpg`)
- **Affichage** de l’image sélectionnée
- **Édition** des métadonnées EXIF :
  - **Auteur** (`Artist`)
  - **Description de l’image** (`ImageDescription`)
- **Ajout de coordonnées GPS**
  - Saisie manuelle (Latitude, Longitude)
  - Convertion automatique en format DMS
  - Enregistrement dans les balises EXIF
- **Affichage sur carte**
  - Visualisation du point GPS sur une carte (via folium)
  - Marqueur personalisé
- **Affichage d'un itineraire**
  - Liste de POI (lieux visités ou rêvés)
  - Marqueurs
- **Téléchargement de l’image modifiée**

---

## Déploiement

L’application est accessible en ligne via **Streamlit Community Cloud** à l’adresse suivante :  
👉 [Voir l'application en ligne](https://tp4-exif-gps.streamlit.app)

---

## Installation locale (optionnelle)

> Testée avec Python 3.11

```bash
# 1. Cloner le dépôt
git clone https://github.com/aemetil/streamlit-tp4-exif-gps.git
cd streamlit-tp4-exif-gps

# 2. Installer les dependances
pip install -r requirements.txt

# 3. Lancer l'application Streamlit
streamlit run app.py
```
