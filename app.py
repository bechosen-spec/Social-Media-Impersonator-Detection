import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase
cred_path = "socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json"
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

def sign_up(email, password):
    try:
        user_record = auth.create_user(email=email, password=password)
        st.success(f"Successfully created user {user_record.uid}")
        st.session_state['authenticated'] = True
    except Exception as e:
        st.error(f"Failed to create user: {e}")

def sign_in(email, password):
    try:
        user_record = auth.get_user_by_email(email)
        st.session_state['authenticated'] = True
        st.success(f"Welcome back, {user_record.email}!")
    except Exception as e:
        st.error("User does not exist or wrong password.")

def show_prediction_interface():
        # Personalized welcome message
    st.subheader(f"Welcome!")
    st.write("Let's check if an account is genuine or an impersonator.")

    with st.form(key='impersonator_form'):
        account_name = st.text_input('Account Name')
        username = st.text_input('Username')

        profile_pic = st.selectbox('Profile Picture (1 = Yes, 0 = No)', options=[1, 0])
        name_eq_username = st.selectbox('Name Equals Username (1 = Yes, 0 = No)', options=[1, 0])
        description_length = st.number_input('Description Length', value=100)
        external_url = st.selectbox('External URL (1 = Yes, 0 = No)', options=[1, 0])
        private = st.selectbox('Private Account (1 = Yes, 0 = No)', options=[1, 0])
        posts = st.number_input('Number of Posts', value=10)
        followers = st.number_input('Number of Followers', value=500)
        follows = st.number_input('Number Following', value=300)
        submit_button = st.form_submit_button(label='Predict')

    if submit_button and account_name and username:  # Ensure account name and username are provided
        input_df = pd.DataFrame([[profile_pic, name_eq_username, description_length, external_url, private, posts,
                                  followers, follows]],
                                columns=['profile_pic', 'name==username', 'description_length',
                                         'external URL', 'private', '#posts', '#followers', '#follows'])
        
        # Load your trained model
        model = joblib.load('Social-Media-Impersonator-Detection\social_media_model.joblib')

        # Scale inputs
        scaler = StandardScaler()
        input_df_scaled = scaler.fit_transform(input_df)

        # Make prediction
        prediction = model.predict(input_df_scaled)

        # Fun and engaging result message
        result_message = f"The account '{account_name}' with the username '{username}' is "
        result_message += "likely Genuine. 🎉" if prediction == 0 else "likely an Impersonator. 🚨"

        if prediction == 0:
            st.success(result_message)
        else:
            st.error(result_message)

# Main Streamlit UI
st.title('Social Media Impersonator Detection')

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if st.session_state['authenticated']:
    show_prediction_interface()
else:
    menu = ["Sign In", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    email = st.sidebar.text_input("Email", key="email")
    password = st.sidebar.text_input("Password", type="password", key="password")

    if choice == "Sign In":
        if st.sidebar.button("Sign In"):
            sign_in(email, password)
    elif choice == "Sign Up":
        if st.sidebar.button("Sign Up"):
            sign_up(email, password)

    if st.session_state['authenticated']:
        st.experimental_rerun()
