import streamlit as st
import helper
import pickle

# Set the page configuration
st.set_page_config(
    page_title="RepliCheck",            # Title in browser tab
    page_icon="Component 7-2.png",      # Custom favicon (must be in the same directory or give path)
    layout="centered"
)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Custom CSS for dark theme and layout
st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            font-family: 'Arial', sans-serif;
        }
        .header {
            font-size: 28px;
            color: #5b3939;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
            font-weight: 700
        }
        .result {
            font-size: 30px;
            font-weight: bold;
            text-align: center;
            margin-top: 30px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #aaaaaa;
        }
        .input-box {
            margin: auto;
            padding: 20px;
            border-radius: 10px;
            background-color: #1a1a1a;
            box-shadow: 0 4px 8px rgba(255, 255, 255, 0.05);
            width: 80%;
        }
        .prediction-text {
            color: #e74c3c;
        }
        /* Center logo */
        .center-logo {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Display logo at top (replacing the RepliCheck text title)
# Centered logo using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Component 7-2.png", width=200)

# Header
st.markdown("<div class='header'>Enter Two Questions to Check for Duplication</div>", unsafe_allow_html=True)

# Input fields
with st.container():
    q1 = st.text_input('Enter Question 1', key="q1", placeholder="Type your first question here...", label_visibility="collapsed")
    q2 = st.text_input('Enter Question 2', key="q2", placeholder="Type your second question here...", label_visibility="collapsed")

# Prediction
if q1 and q2:
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.markdown("<div class='result prediction-text'>Duplicate</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result' style='color:#2ecc71;'>Not Duplicate</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made with passion by Sam | RepliCheck</div>", unsafe_allow_html=True)
