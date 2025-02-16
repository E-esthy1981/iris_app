import streamlit as st
def main():
    st.title("Interface Web avec Streamlit")

    # Champ de texte
    user_input = st.text_input("Entrez votre nom :")

    # Bouton
    if st.button("Soumettre"):
        st.write(f"Bonjour, {user_input}!")

    # Slider
    value = st.slider("Sélectionnez la longueur des Pétals", 0, 100, 50)
    st.write(f"Valeur sélectionnée : {value}")
    
     # Slider
    value = st.slider("Sélectionnez la largeur des Pétals", 0, 100, 50)
    st.write(f"Valeur sélectionnée : {value}")
    
 # Slider
    value = st.slider("Sélectionnez la longueur des Sépals", 0, 100, 50)
    st.write(f"Valeur sélectionnée : {value}")

 # Slider
    value = st.slider("Sélectionnez la largeur des Sépals", 0, 100, 50)
    st.write(f"Valeur sélectionnée  : {value}")

   if __name__ == "__main__":
    main()
       
st.write("bonjour le monde")

st.title("retour au village")

st.button('Hit me')

