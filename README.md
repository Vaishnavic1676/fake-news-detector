
# 📰 Fake News Detector

A Machine Learning web app built with **Python**, **Flask**, and **HTML/CSS** that detects whether a given news headline or article is *Real* or *Fake*. It is trained on authentic global and Indian news datasets with special focus on recent and local headlines.

---

## 🔍 Features

* ✅ Detects fake and real news
* 🇮🇳 Supports Indian news and headlines
* 🧠 Trained with Logistic Regression + TF-IDF
* 🌐 Interactive UI with Dark/Light mode
* 🔒 Fully offline, no API required

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS (with custom animations)
* **Backend:** Flask
* **ML:** Scikit-learn (Logistic Regression), TF-IDF Vectorizer
* **Data:** Fake.csv, True.csv, Indian datasets (custom)

---

## 🚀 How to Run Locally

1. **Clone this repo:**

```bash
git clone https://github.com/Vaishnavic1676/fake-news-detector.git
cd fake-news-detector
```

2. **Install requirements:**

```bash
pip install -r requirements.txt
```

*(If no requirements.txt, manually install Flask + sklearn + nltk)*

3. **Run the app:**

```bash
python app.py
```

4. **Visit:**

```
http://127.0.0.1:5000
```

---

## 🧠 Sample Input

> "ISRO launches Aditya L1 mission"

### Output:

✅ Real News (if trained with correct dataset)

---

## 📁 Project Structure

```
├── app.py
├── load_data.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── Fake.csv / True.csv
├── indian_news.csv / headlines.csv
├── vectorizer.pkl / fake_news_model.pkl
```

---

## 👩‍💻 Author

**Vaishnavi Chougule**
🔗 GitHub: [Vaishnavic1676](https://github.com/Vaishnavic1676)


---

## 📜 License

This project is open-source and available under the MIT License.

---
