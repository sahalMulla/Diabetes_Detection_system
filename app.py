import pandas as pd 
import streamlit as st 
import pickle

# Load the model
with open('diabetes_model_1.pkl', 'rb') as pkl:
    classifier = pickle.load(pkl)

def main():
    # CSS Styling
    st.markdown("""
    <style>
        .block-container {
            padding: 1rem 2rem;
            max-width: 1200px;
            margin: auto;
            font-family: 'Poppins', sans-serif;
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap');

    /* Apply Montserrat globally */
    * {
        font-family: 'Montserrat', sans-serif !important;
    }
        
        .outer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top:40px;
        }

        .header-image {
            flex: 1;
            text-align: center;
        }

        .header-image img {
            height: 220px;
            border-radius: 18px;
            max-width: 100%;
        }

        .center-title {
            flex: 2;
            text-align: center;
        }

        .title-text h1 {
            font-size: 40px;
            color: #336600;
            margin: 0;
            font-family: 'Montserrat', sans-serif !important;
        }

        .subtitle-text {
            font-size: 20px;
            margin-top: 8px;
            color: #4d6600;
            font-family: 'Montserrat, sans-serif !important;
        }

        .custom-label {
            font-size: 22px;
            font-weight: 600;
            margin-bottom: -50px;
            font-family: 'Montserrat', sans-serif !important;
        }

        div.stButton > button {
            background-color: #336600;
            color: white !important;
            padding: 8px 30px;
            font-size: 16px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            white-space: nowrap;
        }

div.stButton > button:hover {
    color: white !important;
    background-color: #4d6600 !important;
}


        .finalmsg {
            margin-top: 30px;
            margin-bottom: 10px;
            font-size: 25px;
            font-weight: bold;
            color: #ff0000;
            text-decoration: underline;
            text-align: center;
            font-family: 'Montserrat', sans-serif !important;
        }

        @media (max-width: 768px) {
            .outer {
                flex-direction: column;
                align-items: center;
                gap: 20px;
            }
        }

        @media (max-width: 880px) {
            .stColumns {
                flex-direction: column !important;
                gap: 20px !important;
            }
        }

        @media (max-width: 480px) {
            div.stButton > button {
                padding: 10px 20px;
                font-size: 14px;
                white-space: normal;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # Placeholder for prediction result
    msg_placeholder = st.empty()

    # Header Section
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

    # Input section: 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="custom-label">Pregnancies</div>', unsafe_allow_html=True)
        pregnancies = st.number_input("", min_value=0, max_value=20, value=0, step=1, key="pregnancies")

        st.markdown('<div class="custom-label">Skin Thickness</div>', unsafe_allow_html=True)
        skin_thickness = st.number_input("", min_value=0, max_value=100, value=0, step=1, key="skin_thickness")

        st.markdown('<div class="custom-label">Diabetes Pedigree Function</div>', unsafe_allow_html=True)
        diabetes_pedigree = st.number_input("", min_value=0.0, max_value=3.0, value=0.0, step=0.01, key="diabetes_pedigree")

    with col2:
        st.markdown('<div class="custom-label">Age</div>', unsafe_allow_html=True)
        age = st.number_input("", min_value=0, max_value=120, value=0, step=1, key="age")

        st.markdown('<div class="custom-label">Glucose</div>', unsafe_allow_html=True)
        glucose = st.number_input("", min_value=0, max_value=300, value=0, step=1, key="glucose")

        st.markdown('<div class="custom-label">Blood Pressure</div>', unsafe_allow_html=True)
        blood_pressure = st.number_input("", min_value=0, max_value=200, value=0, step=1, key="blood_pressure")

    with col3:
        st.markdown('<div class="custom-label">Insulin</div>', unsafe_allow_html=True)
        insulin = st.number_input("", min_value=0, max_value=900, value=0, step=1, key="insulin")

        st.markdown('<div class="custom-label">BMI</div>', unsafe_allow_html=True)
        bmi = st.number_input("", min_value=0.0, max_value=70.0, value=0.0, step=0.1, key="bmi")

    # Predict Button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        predict_btn = st.button("PREDICT PROBABILITY")

    # Prediction Logic
    if predict_btn:
        res = classifier.predict([[pregnancies, skin_thickness, diabetes_pedigree, age, glucose, blood_pressure, insulin, bmi]])
        msg = "✅ Assessment shows no diabetes risk." if res[0] == 0 else "⚠️ Assessment indicates potential diabetes risk."
        msg_placeholder.markdown(f"<div class='finalmsg'>{msg}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
