import streamlit as st

st.title("Dalle-3")

user_input = st.text_input ("Générer une image facilement juste ici : ")

st.write (user_input)

# Créer un champ d'entrée dans la barre latérale pour la clé API
api_key = st.sidebar.text_input("Entrez votre clé DALL-E API :", type="password")

# Bouton pour valider l'entrée
if st.sidebar.button("Valider la clé API"):
    if api_key:
        st.success("Clé API enregistrée avec succès !")
    else:
        st.error("Veuillez entrer une clé API valide.")
        
#Intéraction avec OpenAI
from openai import OpenAI
client = OpenAI(api_key=sidebar_input)

prompt = "A cute baby sea otter"

image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url

#Affichage de l'image
st.image(image_url)
