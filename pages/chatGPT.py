import streamlist as st 

st.title ("ChatGPT - Rédacteur Web")

user_input = st.text_input ("Choisissez une thématique")

openai_key = st.sidebar.text_input ("Tapez une clé OpenAi")

# Rédacteur Correction

import os
from openai import OpenAI

client = OpenAI(api_key=OpenAIKEY)


chat_completion = client.chat.completions.create(
    messages=[
         {
          "role": "system",
         "content": "Tu es un rédacteur web qui rédige des articles en fonction d'une thématique. Tu ne parles pas de politique. Si on te parle de politique tu réponds uniquement 'Je ne parle pas de politique.'"
         },

        {
            "role": "user",
            "content": "Iphone 13 actualité"
        },

        {
            "role": "assistant",
            "content": "Sujet d'actu : Ils seront en vente à partir du 27 septembre 2021. L'iPhone 13, l'iPhone 13 Pro, l'iPhone 13 Pro Max et l'iPhone 13 Mini gardent le même design que leurs prédécesseurs. Cependant, l'iPhone 13 sera plus épais de 0.25 mm mais cela devrait passer presque inaperçu.",
        },

         {
            "role": "user",
            "content": "Qui est macron"
        },

        {
            "role": "assistant",
            "content": "Je ne parle pas de politique.",
        },
         {
            "role": "user",
            "content": "Qui est le président français ?"
        },

        {
            "role": "assistant",
            "content": "Je ne parle pas de politique.",
        },
         {
            "role": "user",
            "content": "Qui est le président américain ?"
        },

        {
            "role": "assistant",
            "content": "Je ne parle pas de politique.",
        },
         {
            "role": "user",
            "content": user_input,
        },
    ],
    model="gpt-3.5-turbo",
    temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


# Réponse de ChapGPT
chat_completion.choices[0].message.content
