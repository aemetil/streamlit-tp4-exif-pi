# *******************************************************
# Nom ......... : app.py
# Rôle ........ : Application Streamlit pour éditer les métadonnées EXIF d'une image
# Auteur ...... : Alberto E.
# Version ..... : V0.1 du 26/05/2025
# Licence ..... : Réalisé dans le cadre du cours Outils Collaboratifs (TP4)
# Usage ....... : streamlit run app.py
# *******************************************************

import streamlit as st
from PIL import Image
import piexif
import io
import folium
from streamlit_folium import st_folium

# Titre de l'application
st.set_page_config(page_title="Éditeur EXIF", layout="centered")
st.markdown("### Éditeur de métadonnées EXIF (avec piexif)")

# Fonction pour convertir des coordonnées décimales en DMS (degrés, minutes, secondes)
def convertir_en_dms(valeur):
    degres = int(valeur)
    minutes = int((valeur - degres) * 60)
    secondes = int((valeur - degres - minutes / 60) * 3600 * 100)
    return [(degres, 1), (minutes, 1), (secondes, 100)]

# Upload de l'image JPEG
fichier = st.file_uploader("Importer une image JPEG", type=["jpg", "jpeg"])

if fichier:
    image = Image.open(fichier)
    st.image(image, caption="Image chargée", use_container_width=True)

    # Chargement des données EXIF avec piexif
    exif_bytes = image.info.get("exif")
    exif_dict = piexif.load(exif_bytes) if exif_bytes else {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    st.subheader("Champs modifiables")

    # Champs modifiables (artiste, description)
    artiste = exif_dict["0th"].get(piexif.ImageIFD.Artist, b"").decode("utf-8", errors="ignore")
    description = exif_dict["0th"].get(piexif.ImageIFD.ImageDescription, b"").decode("utf-8", errors="ignore")

    nouveau_artiste = st.text_input("Auteur de l'image", value=artiste)
    nouvelle_desc = st.text_input("Description de l’image", value=description)

    #saisie des coordonnées GPS (décimales)
    st.subheader("Coordonnées GPS à insérer")

    latitude = st.number_input("Latitude (ex: 48.8566)", format="%.6f", value=48.8566)
    longitude = st.number_input("Longitude (ex: 2.3522)", format="%.6f", value=2.3522)
    
    # Creation d'une carte centrée sur le coordonnées GPS
    st.subheader("Carte de localisation (selon les coordonnées GPS saisies)")
    carte = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], tooltip="Emplacement GPS").add_to(carte)

    # Bouton pour modifier & télécharger
    if st.button("Enregistrer les métadonnées EXIF"):
        # Mise à jour des métadonnées texte
        exif_dict["0th"][piexif.ImageIFD.Artist] = nouveau_artiste.encode("utf-8")
        exif_dict["0th"][piexif.ImageIFD.ImageDescription] = nouvelle_desc.encode("utf-8")
        
        # Affichage de la carte dans streamlit
        st_folium(carte, width=700, height=500)

        # Ajout des coordonnées GPS
        lat_ref = "N" if latitude >= 0 else "S"
        lon_ref = "E" if longitude >= 0 else "W"
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = lat_ref.encode()
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = convertir_en_dms(abs(latitude))
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = lon_ref.encode()
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = convertir_en_dms(abs(longitude))

        # Insertion et sauvegarde
        exif_bytes_new = piexif.dump(exif_dict)
        tampon = io.BytesIO()
        image.save(tampon, format="jpeg", exif=exif_bytes_new)

        st.success("Métadonnées EXIF mises à jour avec succès !")
        st.download_button(
            label="📥 Télécharger l’image modifiée",
            data=tampon.getvalue(),
            file_name="image_modifiee_gps.jpg",
            mime="image/jpeg"
        )