import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase
cred = credentials.Certificate("C:\Users\Boniface\Social-Media-Impersonator-Detection\socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json")
firebase_admin.initialize_app(cred)

def sign_up(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return True, user
    except Exception as e:
        return False, str(e)

def sign_in(email, password):
    try:
        user = auth.get_user_by_email(email)
        # In a real app, you would now compare the password hashes
        return True, user
    except Exception as e:
        return False, str(e)

# Streamlit UI
st.title("Firebase Auth Example")

menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")
elif choice == "Login":
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.button("Login"):
        success, user = sign_in(email, password)
        if success:
            st.success(f"Logged In as {user.email}")
        else:
            st.warning("Incorrect Credentials")

elif choice == "SignUp":
    new_email = st.sidebar.text_input("Email")
    new_password = st.sidebar.text_input("New Password", type='password')
    if st.sidebar.button("SignUp"):
        success, user = sign_up(new_email, new_password)
        if success:
            st.success("Created Account")
            st.balloons()
        else:
            st.error(user)
