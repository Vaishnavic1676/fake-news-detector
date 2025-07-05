import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# 📥 Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")
indian = pd.read_csv("indian_news.csv")
headline = pd.read_csv("headline_news.csv")
fact = pd.read_csv("indian_fact_news.csv")
extra = pd.read_csv("extra_indian_headlines.csv")
more = pd.read_csv("more_current_headlines.csv")  # ✅ NEWEST

# 🏷️ Add labels if needed
fake["label"] = 0
true["label"] = 1
# indian, headline, fact, extra, more already have 'label' column

# ⚖️ Balance Fake & True (only original)
min_len = min(len(fake), len(true))
fake = fake.sample(n=min_len, random_state=42)
true = true.sample(n=min_len, random_state=42)

# 🔗 Combine all datasets
data = pd.concat([fake, true, indian, headline, fact, extra, more], ignore_index=True)
data = data.sample(frac=1).reset_index(drop=True)

print("✅ Combined dataset:")
print(data["label"].value_counts())

# 🔤 Download stopwords
nltk.download("stopwords")

# 🧹 Preprocessing
def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

data["clean_text"] = data["text"].apply(preprocess)

print("\n🧹 Sample cleaned news text:")
print(data[["text", "clean_text"]].head(1))

# 🔢 Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data["clean_text"])
y = data["label"]

print("\n✅ Vectorization complete!")
print(f"Text data shape (X): {X.shape}")
print(f"Labels shape (y): {y.shape}")

# 🔀 Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n📊 Training and testing split complete!")
print(f"Training data: {X_train.shape}, Labels: {y_train.shape}")
print(f"Testing data: {X_test.shape}, Labels: {y_test.shape}")

# 🤖 Train
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# 🎯 Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🤖 Model training complete!")
print(f"✅ Accuracy after full Indian + current data: {accuracy * 100:.2f}%")

# 💾 Save
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("💾 Model and vectorizer saved as .pkl files!")

# 🧪 Final test
sample_text = data[data['label'] == 1].iloc[0]['text']
processed = preprocess(sample_text)
vector = vectorizer.transform([processed])
sample_pred = model.predict(vector)

print("\n🧪 Prediction on known REAL sample:")
print(f"Original: {sample_text[:100]}...")
print("Prediction =", "Real ✅" if sample_pred[0] == 1 else "Fake ❌")
