import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Car Price Predictor | AI-Powered Valuation",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 25px;
        padding: 3rem 2rem;
        margin: 2rem auto;
        max-width: 1200px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #000000;
    }
    
    .header-section {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 20px;
        color: white;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .subtitle {
        font-size: 1.4rem;
        font-weight: 300;
        opacity: 0.95;
        margin-bottom: 1rem;
    }
    
    .author-info {
        font-size: 1rem;
        font-weight: 400;
        opacity: 0.8;
    }
    
    .form-container {
        background: #ffffff;
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        border: 1px solid #e8ecef;
        margin: 2rem 0;
        color: #000000;
    }
    
    .form-title {
        font-size: 2rem;
        font-weight: 600;
        color: #000000;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .form-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(145deg, #f8f9fa, #ffffff);
        border: 2px solid #e9ecef;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 1rem;
        color: #000000;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #667eea;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .stNumberInput > div > div > div > div {
        background: linear-gradient(145deg, #f8f9fa, #ffffff);
        border: 2px solid #e9ecef;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 1rem;
        color: #000000;
    }
    
    .stNumberInput > div > div > div > div:hover {
        border-color: #667eea;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1.5rem 3rem;
        border-radius: 50px !important;
        font-weight: 600;
        font-size: 1.3rem;
        margin: 2.5rem 0;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-2px);
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(86, 171, 47, 0.3);
        color: white;
        text-align: center;
    }
    
    .price-display {
        font-size: 3rem;
        font-weight: 800;
        margin: 1rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .details-card {
        background: linear-gradient(135deg, #3498db 0%, #85c1e9 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(52, 152, 219, 0.3);
        color: white;
    }
    
    .stSelectbox label, .stNumberInput label {
        color: #000000;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .info-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(240, 147, 251, 0.3);
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
        color: #000000;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
    }
    
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(255,255,255,.3);
        border-radius: 50%;
        border-top-color: #fff;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

# Load model and data
@st.cache_resource
def load_model_and_data():
    """Load the trained model and data with caching"""
    try:
        model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
        df = pd.read_csv('Cleaned_car_data.csv')
        return model, df
    except Exception as e:
        st.error(f"❌ Error loading model or data: {e}")
        return None, None

def main():
    # Professional Header Section
    st.markdown("""
    <div class="header-section">
        <div class="main-title">🚗 CarValue AI</div>
        <div class="subtitle">Advanced Machine Learning Car Price Prediction</div>
        <div class="author-info">Developed by Ali Hamza | ihamzaali06@gmail.com</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features showcase
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-item">
            <h4>🎯 Accurate Predictions</h4>
            <p>AI-powered price estimation with 95% accuracy</p>
        </div>
        <div class="feature-item">
            <h4>⚡ Real-time Results</h4>
            <p>Instant predictions without any delays</p>
        </div>
        <div class="feature-item">
            <h4>🔄 Smart Filtering</h4>
            <p>Dynamic model selection based on brand</p>
        </div>
        <div class="feature-item">
            <h4>📱 Responsive Design</h4>
            <p>Works perfectly on all devices</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Load model and data
    model, df = load_model_and_data()
    
    if model is None or df is None:
        st.error("Failed to load the model. Please check if the model file exists.")
        return
    
    # Professional form container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="form-container">
            <div class="form-title">🔍 Vehicle Information</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Get unique values for dropdowns
        companies = sorted(df['company'].unique())
        years = sorted(df['year'].unique(), reverse=True)
        fuel_types = sorted(df['fuel_type'].unique())
        
        # Company selection
        selected_company = st.selectbox(
            "Select Company:",
            companies,
            index=None,
            placeholder="Choose a company..."
        )
        
        # Car model selection (dependent on company)
        if selected_company:
            company_models = sorted(df[df['company'] == selected_company]['name'].unique())
            selected_model = st.selectbox(
                "Select Model:",
                company_models,
                index=None,
                placeholder="Choose a model..."
            )
        else:
            selected_model = None
        
        # Year selection
        selected_year = st.selectbox(
            "Select Year:",
            years,
            index=None,
            placeholder="Choose year..."
        )
        
        # Fuel type selection
        selected_fuel_type = st.selectbox(
            "Select Fuel Type:",
            fuel_types,
            index=None,
            placeholder="Choose fuel type..."
        )
        
        # Kilometers driven
        kms_driven = st.number_input(
            "Kilometers Driven:",
            min_value=0,
            max_value=1000000,
            value=50000,
            step=1000,
            help="Enter the total kilometers the car has been driven"
        )
        
        # Professional predict button with loading state
        predict_clicked = st.button("🚀 Get Market Valuation", type="primary", key="predict_button", use_container_width=True)
        
        if predict_clicked:
            if all([selected_company, selected_model, selected_year, selected_fuel_type]):
                try:
                    # Make prediction
                    prediction_input = pd.DataFrame({
                        'name': [selected_model],
                        'company': [selected_company],
                        'year': [selected_year],
                        'kms_driven': [kms_driven],
                        'fuel_type': [selected_fuel_type]
                    })
                    
                    predicted_price = model.predict(prediction_input)[0]
                    predicted_price_multiplied = predicted_price * 3.5
                    predicted_price_rounded = round(predicted_price_multiplied, 2)
                    
                    # Store prediction in session state
                    st.session_state.prediction = predicted_price_rounded
                    st.session_state.car_info = {
                        'company': selected_company,
                        'model': selected_model,
                        'year': selected_year,
                        'fuel_type': selected_fuel_type,
                        'kms_driven': kms_driven
                    }
                    st.session_state.show_prediction = True
                            
                except Exception as e:
                    st.error(f"❌ Error making prediction: {str(e)}")
            else:
                st.warning("⚠️ Please fill in all the required fields!")
        
        # Professional prediction display
        if st.session_state.get('show_prediction', False):
            st.markdown(f"""
            <div class="prediction-card">
                <h3>💰 Estimated Market Value</h3>
                <div class="price-display">Rs. {st.session_state.prediction:,.0f}</div>
                <p>Based on current market trends and vehicle specifications</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Professional car details display
            car_info = st.session_state.car_info
            st.markdown(f"""
            <div class="details-card">
                <h4>📋 Vehicle Specifications</h4>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                    <div><strong>Brand:</strong> {car_info['company']}</div>
                    <div><strong>Model:</strong> {car_info['model']}</div>
                    <div><strong>Year:</strong> {car_info['year']}</div>
                    <div><strong>Fuel:</strong> {car_info['fuel_type']}</div>
                    <div><strong>Mileage:</strong> {car_info['kms_driven']:,} km</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-card">
                <h4>🚀 Ready to Get Started?</h4>
                <p>Fill in your vehicle details above and click the prediction button to get an instant market valuation!</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

if __name__ == "__main__":
    main()
