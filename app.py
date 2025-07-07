import pandas as pd 
import streamlit as st 
import pickle

# Load the trained diabetes prediction model
with open('diabetes_model.pkl', 'rb') as pkl:
    classifier = pickle.load(pkl)

def main():
    # ===================== CSS Styling =====================
    st.markdown("""
    <style>

        /* Import Montserrat font */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100..900&display=swap');

        /* Apply global font */
        * {
            font-family: 'Montserrat', sans-serif !important;
        }

        /* Page container */
        .block-container {
            padding: 16px 32px;
            max-width: 1300px;
            margin: auto;
        }

        /* Header layout */
        .outer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 30px;
        }

        /* Image container */
        .header-image {
            flex: 1;
            text-align: center;
        }

        .header-image img {
            height: 220px;
            border-radius: 18px;
            width: 100%;
        }

        /* Title container */
        .center-title {
            flex: 2;
            text-align: center;
        }

        .title-text h1 {
            font-size: 38px;
            color: #336600;
            margin: 0;
        }

        .subtitle-text {
            font-size: 18px;
            margin-top: 8px;
            color: #4d6600;
        }

        /* Input labels */
        .custom-label {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: -50px;
        }

        /* Predict button container */
        div.stButton {
            width: 100% !important;
            display: flex;
            justify-content: center;
        }

        /* Predict button style */
        div.stButton > button {
            background-color: #336600;
            color: white !important;
            padding: 12px 15px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            white-space: nowrap;
            margin-top: 10px;
            text-align: center;
        }

        div.stButton > button:hover {
            background-color: #4d6600 !important;
        }

        /* Result message styles */
        .safe-msg {
            margin-top: 30px;
            font-size: 25px;
            font-weight: bold;
            color: #008000;
            text-decoration: underline;
            text-align: center;
            animation: fadeSlideUp 0.8s ease forwards;
        }

        .warning-msg {
            margin-top: 30px;
            font-size: 25px;
            font-weight: bold;
            color: #ff0000;
            text-decoration: underline;
            text-align: center;
            animation: fadeSlideUp 0.8s ease forwards;
        }

        /* Animation keyframes */
        @keyframes fadeSlideUp {
            0% {
                opacity: 0;
                transform: translateY(20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive layout for smaller screens */
        @media (max-width: 880px) {
            .outer,
            .stColumns {
                flex-direction: column !important;
                align-items: center;
                gap: 20px !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # ===================== Placeholder for Prediction =====================
    msg_placeholder = st.empty()

    # ===================== Header Section =====================
    st.markdown("""
    <div class='outer'>
        <div class='header-image'>
            <img src='https://etimg.etb2bimg.com/photo/87702233.cms' alt='Blood Sugar Levels'>
        </div>
        <div class='title-container center-title'>
            <div class='title-text'><h1>Diabetes Detection System</h1></div>
            <div class='subtitle-text'>Predict the probability of having diabetes using patient data.</div>
        </div>
        <div class='header-image'>
            <img src='https://blog.medkart.in/wp-content/uploads/2024/01/Normal-Blood-Sugar-Levels-image-1024x591.jpg' alt='Blood Sugar Levels'>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ===================== Input Section =====================
    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="custom-label">Pregnancies</div>', unsafe_allow_html=True)
        pregnancies = st.number_input("", min_value=0, max_value=20, value=0, step=1, key="pregnancies")

    with col2:
        st.markdown('<div class="custom-label">Age</div>', unsafe_allow_html=True)
        age = st.number_input("", min_value=0, max_value=120, value=0, step=1, key="age")

    with col3:
        st.markdown('<div class="custom-label">Insulin</div>', unsafe_allow_html=True)
        insulin = st.number_input("", min_value=0, max_value=900, value=0, step=1, key="insulin")

    # Row 2
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown('<div class="custom-label">Skin Thickness</div>', unsafe_allow_html=True)
        skin_thickness = st.number_input("", min_value=0, max_value=100, value=0, step=1, key="skin_thickness")

    with col5:
        st.markdown('<div class="custom-label">Glucose</div>', unsafe_allow_html=True)
        glucose = st.number_input("", min_value=0, max_value=300, value=0, step=1, key="glucose")

    with col6:
        st.markdown('<div class="custom-label">BMI</div>', unsafe_allow_html=True)
        bmi = st.number_input("", min_value=0.0, max_value=70.0, value=0.0, step=0.1, key="bmi")

    # Row 3
    col7, col8 = st.columns(2)
    with col7:
        st.markdown('<div class="custom-label">Diabetes Pedigree Function</div>', unsafe_allow_html=True)
        diabetes_pedigree = st.number_input("", min_value=0.0, max_value=3.0, value=0.0, step=0.01, key="diabetes_pedigree")

    with col8:
        st.markdown('<div class="custom-label">Blood Pressure</div>', unsafe_allow_html=True)
        blood_pressure = st.number_input("", min_value=0, max_value=200, value=0, step=1, key="blood_pressure")

    # ===================== Predict Button =====================
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        predict_btn = st.button("PREDICT PROBABILITY")

    # ===================== Prediction Logic =====================
    if predict_btn:
        res = classifier.predict([[pregnancies, skin_thickness, diabetes_pedigree, age,
                                   glucose, blood_pressure, insulin, bmi]])
        
        if res[0] == 0:
            msg = "✅ Assessment shows no diabetes risk."
            css_class = "safe-msg"
        else:
            msg = "⚠️ Assessment indicates potential diabetes risk."
            css_class = "warning-msg"
        
        msg_placeholder.markdown(f"<div class='{css_class}'>{msg}</div>", unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()