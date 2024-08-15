import streamlit as st
import pickle

# Load the model and CountVectorizer
with open('spam_classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('count_vectorizer.pkl', 'rb') as f:
    c = pickle.load(f)

# Title of the app
st.title('Email Spam Classifier')

# Text input for the user
user_input = st.text_area("Enter the email text")


if st.button("Classify"):
    if user_input.strip() == "":
        st.write("Please enter some text.")
    else:

        user_input_c = c.transform([user_input])


        prediction = model.predict(user_input_c)[0]


        if prediction == 1:
            st.write("This email is classified as **Spam**.")
        else:
            st.write("This email is classified as **Not Spam**.")
