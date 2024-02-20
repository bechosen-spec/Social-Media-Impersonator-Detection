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


# import streamlit as st
# import pandas as pd
# import joblib
# from sklearn.preprocessing import StandardScaler
# import firebase_admin
# from firebase_admin import credentials, firestore, auth

# # Path to your Firebase admin SDK key file
# cred_path = "C:/Users/Boniface/Social-Media-Impersonator-Detection/socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json"

# # Check if the Firebase app is already initialized to prevent re-initialization
# if not firebase_admin._apps:
#     cred = credentials.Certificate(cred_path)
#     firebase_admin.initialize_app(cred)

# # Function to register a new user
# def sign_up(email, password):
#     try:
#         user_record = auth.create_user(email=email, password=password)
#         st.success(f"Successfully created user {user_record.uid}")
#         # You might want to automatically sign in the user here or redirect them to the sign-in page
#         st.session_state['authenticated'] = True  # Optionally auto-authenticate the user upon sign-up
#     except Exception as e:
#         # Handle exceptions, e.g., email already in use
#         st.error(f"Failed to create user: {e}")

# # Function to authenticate a user
# def sign_in(email, password):
#     try:
#         # Here, we're only checking if the user exists in Firebase Authentication.
#         # NOTE: This does not verify the password, which should be handled via Firebase's client SDKs or a secure server-side token exchange.
#         user_record = auth.get_user_by_email(email)
#         if user_record:
#             st.session_state['authenticated'] = True
#             st.success(f"Welcome back, {user_record.email}!")
#     except Exception as e:
#         st.error("User does not exist or wrong password.")


# # Load your trained model
# model = joblib.load('C:/Users/Boniface/Social-Media-Impersonator-Detection/random_forest_model.joblib')

# # Function to scale inputs
# def scale_inputs(input_df):
#     scaler = StandardScaler()
#     scaled_df = scaler.fit_transform(input_df)
#     return scaled_df

# # Main Streamlit UI
# st.title('Social Media Impersonator Detection')

# # Authentication State
# if 'authenticated' not in st.session_state:
#     st.session_state['authenticated'] = False

# # Sign-in and Sign-up Navigation
# if not st.session_state['authenticated']:
#     menu = ["Sign In", "Sign Up"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "Sign In":
#         email = st.sidebar.text_input("Email", key="signin_email")
#         password = st.sidebar.text_input("Password", type="password", key="signin_password")
#         if st.sidebar.button("Sign In"):
#             sign_in(email, password)

#     elif choice == "Sign Up":
#         new_email = st.sidebar.text_input("Email", key="signup_email")
#         new_password = st.sidebar.text_input("Password", type="password", key="signup_password")
#         if st.sidebar.button("Sign Up"):
#             sign_up(new_email, new_password)
# else:
#     # After successful sign-in
#     # Input fields for the impersonator detection model
#     profile_pic = st.selectbox('Profile Picture (1 = Yes, 0 = No)', options=[1, 0])
#     nums_length_username = st.number_input('Ratio of Numbers in Username')
#     fullname_words = st.number_input('Number of Words in Fullname')
#     nums_length_fullname = st.number_input('Ratio of Numbers in Fullname')
#     name_eq_username = st.selectbox('Name Equals Username (1 = Yes, 0 = No)', options=[1, 0])
#     description_length = st.number_input('Description Length')
#     external_url = st.selectbox('External URL (1 = Yes, 0 = No)', options=[1, 0])
#     private = st.selectbox('Private Account (1 = Yes, 0 = No)', options=[1, 0])
#     posts = st.number_input('Number of Posts')
#     followers = st.number_input('Number of Followers')
#     follows = st.number_input('Number Following')

#     # Predict button
#     if st.button('Predict'):
#         input_df = pd.DataFrame([[profile_pic, nums_length_username, fullname_words, nums_length_fullname,
#                                   name_eq_username, description_length, external_url, private, posts,
#                                   followers, follows]],
#                                 columns=['profile_pic', 'nums/length_username', 'fullname_words',
#                                          'nums/length_fullname', 'name==username', 'description_length',
#                                          'external URL', 'private', '#posts', '#followers', '#follows'])
        
#         # Scale inputs
#         input_df_scaled = scale_inputs(input_df)
        
#         # Make prediction
#         prediction = model.predict(input_df_scaled)
        
#         if prediction == 0:
#             st.success('The account is likely Genuine.')
#         else:
#             st.error('The account is likely an Impersonator.')



# import streamlit as st
# import pandas as pd
# import joblib
# from sklearn.preprocessing import StandardScaler
# import firebase_admin
# from firebase_admin import credentials, auth

# # Initialize Firebase
# cred_path = "C:/Users/Boniface/Social-Media-Impersonator-Detection/socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json"
# if not firebase_admin._apps:
#     cred = credentials.Certificate(cred_path)
#     firebase_admin.initialize_app(cred)

# def sign_up(email, password):
#     try:
#         user_record = auth.create_user(email=email, password=password)
#         st.success(f"Successfully created user {user_record.uid}")
#         st.session_state['authenticated'] = True
#     except Exception as e:
#         st.error(f"Failed to create user: {e}")

# def sign_in(email, password):
#     try:
#         user_record = auth.get_user_by_email(email)
#         st.session_state['authenticated'] = True
#         st.success(f"Welcome back, {user_record.email}!")
#     except Exception as e:
#         st.error("User does not exist or wrong password.")

# # Load your trained model
# model = joblib.load('C:/Users/Boniface/Social-Media-Impersonator-Detection/random_forest_model.joblib')

# def scale_inputs(input_df):
#     scaler = StandardScaler()
#     scaled_df = scaler.fit_transform(input_df)
#     return scaled_df

# def show_prediction_interface():
#     st.subheader("Prediction Interface")
#     with st.form(key='impersonator_form'):
#         profile_pic = st.selectbox('Profile Picture (1 = Yes, 0 = No)', options=[1, 0])
#         nums_length_username = st.number_input('Ratio of Numbers in Username', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
#         fullname_words = st.number_input('Number of Words in Fullname', min_value=0, max_value=10, value=2, step=1)
#         nums_length_fullname = st.number_input('Ratio of Numbers in Fullname', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
#         name_eq_username = st.selectbox('Name Equals Username (1 = Yes, 0 = No)', options=[1, 0])
#         description_length = st.number_input('Description Length', min_value=0, value=50)
#         external_url = st.selectbox('External URL (1 = Yes, 0 = No)', options=[1, 0])
#         private = st.selectbox('Private Account (1 = Yes, 0 = No)', options=[1, 0])
#         posts = st.number_input('Number of Posts', min_value=0, value=10)
#         followers = st.number_input('Number of Followers', min_value=0, value=100)
#         follows = st.number_input('Number Following', min_value=0, value=100)
#         submit_button = st.form_submit_button(label='Predict')

#     if submit_button:
#         input_df = pd.DataFrame([[profile_pic, nums_length_username, fullname_words, nums_length_fullname,
#                                   name_eq_username, description_length, external_url, private, posts,
#                                   followers, follows]],
#                                 columns=['profile_pic', 'nums/length_username', 'fullname_words',
#                                          'nums/length_fullname', 'name==username', 'description_length',
#                                          'external URL', 'private', '#posts', '#followers', '#follows'])

#         input_df_scaled = scale_inputs(input_df)
#         prediction = model.predict(input_df_scaled)

#         if prediction == 0:
#             st.success('The account is likely Genuine.')
#         else:
#             st.error('The account is likely an Impersonator.')

# # Main Streamlit UI
# st.title('Social Media Impersonator Detection')

# if 'authenticated' not in st.session_state:
#     st.session_state['authenticated'] = False

# if st.session_state['authenticated']:
#     show_prediction_interface()
# else:
#     menu = ["Sign In", "Sign Up"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "Sign In":
#         email = st.sidebar.text_input("Email", key="signin_email_2")
#         password = st.sidebar.text_input("Password", type="password", key="signin_password_2")
#         if st.sidebar.button("Sign In"):
#             sign_in(email, password)
#     elif choice == "Sign Up":
#         new_email = st.sidebar.text_input("Email", key="signup_email_2")
#         new_password = st.sidebar.text_input("Password", type="password", key="signup_password_2")
#         if st.sidebar.button("Sign Up"):
#             sign_up(new_email, new_password)

import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase
cred_path = "C:/Users/Boniface/Social-Media-Impersonator-Detection/socialmediaproject-493c8-firebase-adminsdk-zgwf6-3086fc067d.json"
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
        model = joblib.load('C:/Users/Boniface/Social-Media-Impersonator-Detection/random_forest_model.joblib')

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
