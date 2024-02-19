# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, auth

# # Initialize Firebase only if it hasn't been initialized yet
# if not firebase_admin._apps:
#     cred_path = "C:/Users/Boniface/Social-Media-Impersonator-Detection/socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json"
#     cred = credentials.Certificate(cred_path)
#     firebase_admin.initialize_app(cred)

# def sign_up(email, password):
#     try:
#         user = auth.create_user(email=email, password=password)
#         return True, user
#     except Exception as e:
#         return False, str(e)

# def sign_in(email, password):
#     try:
#         user = auth.get_user_by_email(email)
#         # In a real app, you would now compare the password hashes
#         return True, user
#     except Exception as e:
#         return False, str(e)

# # Streamlit UI
# st.title("Firebase Auth Example")

# menu = ["Home", "Login", "SignUp"]
# choice = st.sidebar.selectbox("Menu", menu)

# if choice == "Home":
#     st.subheader("Home")
# elif choice == "Login":
#     email = st.sidebar.text_input("Email")
#     password = st.sidebar.text_input("Password", type='password')
#     if st.sidebar.button("Login"):
#         success, user = sign_in(email, password)
#         if success:
#             st.success(f"Logged In as {user.email}")
#         else:
#             st.warning("Incorrect Credentials")

# elif choice == "SignUp":
#     new_email = st.sidebar.text_input("Email")
#     new_password = st.sidebar.text_input("New Password", type='password')
#     if st.sidebar.button("SignUp"):
#         success, user = sign_up(new_email, new_password)
#         if success:
#             st.success("Created Account")
#             st.balloons()
#         else:
#             st.error(user)


import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase-key.json")
firebase_admin.initialize_app(cred)

# Firebase Authentication Functions
def sign_up(email, password):
    # Firebase sign-up logic
    pass

def sign_in(email, password):
    # Firebase sign-in logic
    pass

# Load your trained model
model = joblib.load('random_forest_model.joblib')

# Function to scale inputs
def scale_inputs(input_df):
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(input_df)
    return scaled_df

# Main Streamlit UI
st.title('Social Media Impersonator Detection')

# Authentication State
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Sign-in and Sign-up Navigation
if not st.session_state['authenticated']:
    menu = ["Sign In", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Sign In":
        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Sign In"):
            # Sign-in logic here
            pass

    elif choice == "Sign Up":
        # Sign-up logic here
        pass
else:
    # After successful sign-in
    # Input fields for the impersonator detection model
    profile_pic = st.selectbox('Profile Picture (1 = Yes, 0 = No)', options=[1, 0])
    nums_length_username = st.number_input('Ratio of Numbers in Username')
    fullname_words = st.number_input('Number of Words in Fullname')
    nums_length_fullname = st.number_input('Ratio of Numbers in Fullname')
    name_eq_username = st.selectbox('Name Equals Username (1 = Yes, 0 = No)', options=[1, 0])
    description_length = st.number_input('Description Length')
    external_url = st.selectbox('External URL (1 = Yes, 0 = No)', options=[1, 0])
    private = st.selectbox('Private Account (1 = Yes, 0 = No)', options=[1, 0])
    posts = st.number_input('Number of Posts')
    followers = st.number_input('Number of Followers')
    follows = st.number_input('Number Following')

    # Predict button
    if st.button('Predict'):
        input_df = pd.DataFrame([[profile_pic, nums_length_username, fullname_words, nums_length_fullname,
                                  name_eq_username, description_length, external_url, private, posts,
                                  followers, follows]],
                                columns=['profile_pic', 'nums/length_username', 'fullname_words',
                                         'nums/length_fullname', 'name==username', 'description_length',
                                         'external URL', 'private', '#posts', '#followers', '#follows'])
        
        # Scale inputs
        input_df_scaled = scale_inputs(input_df)
        
        # Make prediction
        prediction = model.predict(input_df_scaled)
        
        if prediction == 0:
            st.success('The account is likely Genuine.')
        else:
            st.error('The account is likely an Impersonator.')
