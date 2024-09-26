import streamlit as st

# Titre
st.title(" Mon formulaire")

# Texte
st.write ("Ceci est un formulaire de contact")

#Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write (user_input)


#image 
st.image("https://www.radiofrance.fr/s3/cruiser-production/2021/09/6be9e0c8-44b5-4b1a-b7a1-60f65971301d/1200x680_pop-smoke.jpg")

#Sidebar
st.sidebar.title ("Balladin Suhayl")
