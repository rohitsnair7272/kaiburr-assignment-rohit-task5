# 📢 Consumer Complaint Classification using Gemini AI

## 📌 Project Overview

This project classifies consumer complaints into predefined categories using **Google Gemini AI** and evaluates its performance. The classification happens in **real-time** through a **Streamlit-based UI**. Additionally, the **evaluate.py** script processes a dataset row by row and calculates performance metrics (**accuracy, precision, recall, and F1-score**).

---

## 🚀 Features

- **Real-time Complaint Classification** using Gemini AI API.
- **User-friendly Streamlit UI** to input and classify complaints.
- **Performance Evaluation** by processing dataset rows and comparing predictions with actual labels.

---

## 📂 Project Structure

- `streamlit_app.py`: Streamlit UI for real-time classification.
- `evaluate.py`: Script for batch processing and model evaluation.
- `.env`: Stores the API key securely.
- `requirements.txt`: Dependencies for the project.
- `complaints.csv`: Dataset file (ignored in Git).

---

## 🔧 Setup Instructions

### 1️⃣ Create a Virtual Environment

To ensure a clean workspace, create a virtual environment:

```bash
python -m venv venv
```

### 2️⃣ Activate the Virtual Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

Create a **.env** file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

> **Note**: The `.env` file is included in `.gitignore` to prevent exposing API keys.

### 5️⃣ Run the Streamlit App

To launch the Streamlit UI for real-time classification:

```bash
streamlit run streamlit_app.py
```

### 6️⃣ Run the Performance Evaluation Script

To process the dataset and evaluate the model:

```bash
python evaluate.py
```

---

## 🎨 Streamlit UI Overview

- **Enter a consumer complaint** into the text box.
- **Click 'Classify Complaint'** to get the predicted category.
- **View category output** and handle errors if they occur.

**📌 Screenshot:** ![image alt](https://github.com/rohitsnair7272/kaiburr-assignment-rohit-task5/blob/main/frontend.png?raw=true)

---

## 📊 Performance Evaluation

The **evaluate.py** script processes the dataset row by row and computes model performance metrics.

**📌 Screenshot:** _(Replace with your actual screenshot)_

### 🔹 Sample Metrics Output

```
📊 Model Performance Evaluation 📊
✅ Accuracy: 0.9292
✅ Precision: 0.9292
✅ Recall: 0.9292
✅ F1 Score: 0.9292
```

---

## 📩 Future Improvements

- Integrate **batch classification** for multiple complaints at once.
- Improve category matching **by fine-tuning Gemini's prompt engineering**.
- Implement **advanced NLP preprocessing** to enhance classification accuracy.

---

## 📝 Conclusion

This project demonstrates **real-time consumer complaint classification** using **Google Gemini AI** and **performance evaluation** via dataset comparison. The **Streamlit UI** makes classification **interactive**, while **evaluate.py** ensures objective model assessment.

🔥 _Feel free to contribute, suggest improvements, or fork this project!_
