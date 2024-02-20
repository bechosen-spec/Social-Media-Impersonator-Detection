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
    st.subheader("Prediction Interface")
    with st.form(key='impersonator_form'):
        profile_pic = st.selectbox('Profile Picture (1 = Yes, 0 = No)', options=[1, 0])
        nums_length_username = st.number_input('Ratio of Numbers in Username', value=0.0, step=0.01)
        fullname_words = st.number_input('Number of Words in Fullname', value=1, step=1)
        nums_length_fullname = st.number_input('Ratio of Numbers in Fullname', value=0.0, step=0.01)
        name_eq_username = st.selectbox('Name Equals Username (1 = Yes, 0 = No)', options=[1, 0])
        description_length = st.number_input('Description Length', value=100)
        external_url = st.selectbox('External URL (1 = Yes, 0 = No)', options=[1, 0])
        private = st.selectbox('Private Account (1 = Yes, 0 = No)', options=[1, 0])
        posts = st.number_input('Number of Posts', value=10)
        followers = st.number_input('Number of Followers', value=500)
        follows = st.number_input('Number Following', value=300)
        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        input_df = pd.DataFrame([[profile_pic, nums_length_username, fullname_words, nums_length_fullname,
                                  name_eq_username, description_length, external_url, private, posts,
                                  followers, follows]],
                                columns=['profile_pic', 'nums/length_username', 'fullname_words',
                                         'nums/length_fullname', 'name==username', 'description_length',
                                         'external URL', 'private', '#posts', '#followers', '#follows'])
        # Load your trained model
        model = joblib.load('random_forest_model.joblib')

        # Scale inputs
        scaler = StandardScaler()
        input_df_scaled = scaler.fit_transform(input_df)

        # Make prediction
        prediction = model.predict(input_df_scaled)

        if prediction == 0:
            st.success('The account is likely Genuine.')
        else:
            st.error('The account is likely an Impersonator.')

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
