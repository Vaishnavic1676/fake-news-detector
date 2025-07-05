from flask import Flask, render_template, request
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# ✅ Preprocessing function
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Flask app
app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        news_text = request.form["news"]
        processed = preprocess(news_text)
        vector = vectorizer.transform([processed])
        prediction = model.predict(vector)[0]
        result = "Real ✅" if prediction == 1 else "Fake ❌"
        return render_template("index.html", prediction=result)

# Run server
if __name__ == "__main__":
    app.run(debug=True)
