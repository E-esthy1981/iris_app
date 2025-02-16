import streamlit as st
def main():
    st.title("Interface Web avec Streamlit")

    # Champ de texte
    user_input = st.text_input("Entrez votre nom :")

    # Bouton
    if st.button("Soumettre"):
        st.write(f"Bonjour, {user_input}!")

    # Sélection dans une liste déroulante
    option = st.selectbox("Choisissez une option :", ["Option 1", "Option 2", "Option 3"])
    st.write(f"Vous avez choisi : {option}")

    # Slider
    value = st.slider("Sélectionnez une valeur", 0, 100, 50)
    st.write(f"Valeur sélectionnée : {value}")

    # Affichage d'une image
    st.image("https://picsum.photos/200/300", caption="Image aléatoire")

if __name__ == "__main__":
    main()
       
st.write("bonjour le monde")

st.title("retour au village")

st.button('Hit me')

