import streamlit as st
def main():
    st.title("Interface Web avec Streamlit")
    st.sidebar.header("Analyse des données")
    st.sidebar.text("selectionner un des menus suivants pour avancer ")
    st.title("TP IA CREATION D'UN SITE WEB")
    st.header("Partie 1")
   
    # Champ de texte
    user_input = st.text_input("Entrez votre nom :")

    # Bouton
    if st.button("Soumettre"):
        st.write(f"Bonjour, {user_input}!")

    # Sélection dans une liste déroulante
    option = st.selectbox("Choisissez une option :", ["Accueil", "Descriptions", "Blog", "Actualités"])
    st.write(f"Vous avez choisi : {option}")

    # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"entrée la longueur des Sépals : {value}")
    

if __name__ == "__main__":
    main()
       
st.write("bonjour le monde")

st.title("retour au village")

st.button('Hit me')

