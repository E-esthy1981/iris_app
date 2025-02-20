import streamlit as st
def main():
    st.title("Interface Web avec Streamlit")
    st.sidebar.header("Analyse des données")
    st.sidebar.text("selectionnerun des menus suivants pour continuer")


    # Champ de texte
    user_input = st.text_input("Entrez votre nom :")

    # Bouton
    if st.button("Soumettre"):
        st.write(f"Bonjour, {user_input}!")

    # Sélection dans une liste déroulante
    #option = st.selectbox("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
    #st.write(f"Vous avez choisi : {option}")

    # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"entrée la longueur des Sépals : {value}")
      # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"entrée la largeur des Sépals : {value}")
      # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"entrée la longeur des Pétals : {value}")
      # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"entrée la lageur des Pétals : {value}")

if __name__ == "__main__":
    main()
       
st.write("bonjour le monde")

st.title("retour au village")

st.button('Hit me')

