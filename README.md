# TP4 - Streamlit : EXIF + PI

![Apercu de l'accueil de l'application](.github/cover.png)

Ce projet a été réalisé dans le cadre du TP4 du cours **Outils Collaboratifs**.  
Il s'agit d'une **application Streamlit multipage** permettant de:

- Modifier les métadonnées EXIF d'une image (TP4.2)
- Ajouter ou modifier les coordonnées GPS d'une image
- Visualiser l'image et sa geolocalisation sur une carte
- Afficher des lieux visités ou rêvés sur une carte interactive
- Rechercher une date de naissance dans le permier de million decimales de PI (TP4.3)

---

## Pages disponibles

- **TP4.2 - Edition des metadonnées EXIF d'une image**
- **TP4.3 - Recherche dans les decimales de PI**

## Fonctionnalités principales

### TP4.2 : Metadonnées EXIF + Cartographie

- **Import d'une image JPEG**
- **Affichage de l’image sélectionnée**
- **Édition des métadonnées EXIF** :
  - Auteur (`Artist`)
  - Description de l’image (`ImageDescription`)
  - Coordonnées GPS(Latitude, Longitude en format DMS)
- **Visualisation sur carte (via folium)** :
  - Position GPS actuelle
  - POI des lieux visités ou revés
- **Téléchargement de l’image modifiée**

## TP4.3 : Decimales de PI

- **Recherche d'une date de naissance** (format `JJMMAAAA`)
- **Affichage de la position si trouvée**
- **Jour de la semaine correspondant à la date**
- **Calcul et comparaison**:
  - Somme des 20 premières decimales
  - Somme des \(12^2\) premières décimales
    **Integration d'une vidéo pedagogique** sur la somme des entiers naturels \(\sum\_{n=1}^\infty n = -\frac{1}{12}\)

---

## Déploiement

L’application est accessible en ligne via **Streamlit Community Cloud** à l’adresse suivante :  
👉 [Voir l'application en ligne](https://tp4-exif-pi.streamlit.app)

---

## Installation locale (optionnelle)

> Testée avec Python 3.11

```bash
# 1. Cloner le dépôt
git clone https://github.com/aemetil/streamlit-tp4-exif-pi.git
cd streamlit-tp4-exif-gps

# 2. Installer les dependances
pip install -r requirements.txt

# 3. Lancer l'application Streamlit
streamlit run app.py
```
