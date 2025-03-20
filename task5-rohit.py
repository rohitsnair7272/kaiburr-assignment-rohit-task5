import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Google Gemini API Endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

# Complaint categories
CATEGORIES = {
    0: "Credit reporting, repair, or other",
    1: "Debt collection",
    2: "Consumer Loan",
    3: "Mortgage"
}

# Function to classify consumer complaints
def classify_complaint(complaint_text):
    headers = {"Content-Type": "application/json"}
    prompt = f"Classify this consumer complaint into one of these categories: {CATEGORIES}. Complaint: {complaint_text}"
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        model_response = result["candidates"][0]["content"]["parts"][0]["text"].strip()
        
        # Determine category based on model response
        for key, value in CATEGORIES.items():
            if value.lower() in model_response.lower():
                return key, value
        
        return None, "Unknown Category"
    else:
        return None, f"Error: {response.text}"

# Streamlit UI
st.title("📢 Real-Time Consumer Complaint Classifier")
st.markdown("Classify consumer complaints into predefined categories using Gemini AI.")

# Text input for user complaint
complaint_text = st.text_area("Enter Consumer Complaint:")

if st.button("Classify Complaint"):
    if complaint_text.strip():
        category_id, category_name = classify_complaint(complaint_text)
        
        if category_id is not None:
            st.success(f"**Category:** {category_name} (ID: {category_id})")
        else:
            st.error(category_name)  # Show error message
    else:
        st.warning("Please enter a complaint before classifying.")

