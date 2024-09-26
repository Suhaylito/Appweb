import openai
import streamlit as st

# Titre de l'application
st.title("DALL-E Image Generator")

# Champ d'entrée pour l'utilisateur
user_input = st.text_input("Générer une image facilement juste ici :")

# Créer un champ d'entrée dans la barre latérale pour la clé API
api_key = st.sidebar.text_input("Entrez votre clé DALL-E API :", type="password")

# Validation de la clé API
if api_key:
    # Configurer la clé API pour OpenAI
    openai.api_key = api_key
    
    # Bouton pour générer l'image
    if st.button("Générer une image"):
        if user_input:
            # Générer l'image avec DALL-E
            try:
                response = openai.Image.create(
                    prompt=user_input,
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                # Afficher l'image générée
                st.image(image_url, caption=f"Image générée pour : {user_input}")
            except Exception as e:
                st.error(f"Erreur lors de la génération de l'image : {e}")
        else:
            st.error("Veuillez entrer une description pour générer l'image.")
else:
    st.warning("Veuillez entrer votre clé API DALL-E dans la barre latérale.")
