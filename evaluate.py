import pandas as pd
import requests
import os
import time
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load API Key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") #.env file is included in gitignore so the api key isnt revealed

# Google Gemini API Endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

# Define categories for classification
CATEGORIES = {
    "Credit reporting or other personal consumer reports": 0,
    "Debt collection": 1,
    "Payday loan, title loan, personal loan, or advance loan": 2,
    "Mortgage": 3
}

# Function to classify consumer complaints using Gemini AI
def classify_complaint(complaint_text):
    headers = {"Content-Type": "application/json"}
    prompt = f"Classify this consumer complaint into one of these categories: {list(CATEGORIES.keys())}. Complaint: {complaint_text}"

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        model_response = result["candidates"][0]["content"]["parts"][0]["text"].strip()

        # Determine category based on model response
        for category_name, category_id in CATEGORIES.items():
            if category_name.lower() in model_response.lower():
                return category_id
        
        return -1  # Unknown Category
    else:
        return -1  # API error or invalid response

# Load dataset in chunks to handle large file size
DATASET_PATH = "complaints.csv"  #the csv file is also included in gitignore because of its size
chunk_size = 1000  # Process 1000 rows at a time

actual_labels = []
predicted_labels = []

# Process dataset row by row
for chunk in pd.read_csv(DATASET_PATH, chunksize=chunk_size):
    for index, row in chunk.iterrows():
        product = row["Product"]
        complaint_text = row["Consumer complaint narrative"]

        if pd.isna(complaint_text):  # Skip if complaint text is empty
            continue

        # Get actual category from "Product"
        actual_category = CATEGORIES.get(product, -1)

        # Get AI predicted category
        predicted_category = classify_complaint(complaint_text)

        if actual_category != -1 and predicted_category != -1:
            actual_labels.append(actual_category)
            predicted_labels.append(predicted_category)

    print(f"Processed {len(actual_labels)} rows...")

    # Stop early if we reach 65 rows (adjustable)
    if len(actual_labels) >= 65:
        break

# Calculate Performance Metrics
accuracy = accuracy_score(actual_labels, predicted_labels)
precision = precision_score(actual_labels, predicted_labels, average="weighted", zero_division=0)
recall = recall_score(actual_labels, predicted_labels, average="weighted", zero_division=0)
f1 = f1_score(actual_labels, predicted_labels, average="weighted", zero_division=0)

# Print Results
print("\n📊 Model Performance Evaluation 📊")
print(f"✅ Accuracy: {accuracy:.4f}")
print(f"✅ Precision: {precision:.4f}")
print(f"✅ Recall: {recall:.4f}")
print(f"✅ F1 Score: {f1:.4f}")
