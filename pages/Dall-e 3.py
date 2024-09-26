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
