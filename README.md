# 🛡️ Phishing URL Detector

An ML-powered web application that detects phishing URLs in real-time using a trained Random Forest classifier. Built with Flask, scikit-learn, and an in-memory database for quick demos.

---

## 🚀 Features

- **Real-Time URL Scanning** — Paste any URL and get an instant phishing/safe verdict with a confidence score.
- **11-Feature Extraction Engine** — Analyzes URL length, HTTPS presence, IP-based domains, subdomain count, URL entropy, suspicious keywords, shortened links, and more.
- **ML-Powered Detection** — Uses a Random Forest classifier trained on 3,000 synthetic samples with 200 estimators.
- **Interactive Dashboard** — View scan history, phishing vs. safe counts, and recent scan results.
- **Beautiful UI** — Clean, modern landing page and scanner interface.

---

## 📁 Project Structure

```
phishi/
├── app.py                  # Flask application (routes & API)
├── feature_extractor.py    # Extracts 11 features from a URL
├── model_handler.py        # Loads the ML model & runs predictions
├── db_handler.py           # In-memory database handler
├── train_model.py          # Script to train the Random Forest model
├── requirements.txt        # Python dependencies
├── models/
│   └── phishing_model.pkl  # Pre-trained model (auto-generated)
└── templates/
    ├── landing.html         # Landing page
    ├── index.html           # URL scanner page
    └── dashboard.html       # Analytics dashboard
```

---

## 🛠️ Getting Started

### Prerequisites

- **Python 3.10+** installed on your system
- **pip** (Python package manager)
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/SneakyRam/phishing.git
cd phishing
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the ML Model (Optional)

A pre-trained model (`models/phishing_model.pkl`) is already included. If you want to retrain it:

```bash
python train_model.py
```

### 5. Run the Application

```bash
python app.py
```

The app will start on **http://localhost:5001**

### 6. Open in Browser

| Page | URL |
|------|-----|
| 🏠 Landing Page | [http://localhost:5001/](http://localhost:5001/) |
| 🔍 URL Scanner | [http://localhost:5001/scanner](http://localhost:5001/scanner) |
| 📊 Dashboard | [http://localhost:5001/dashboard](http://localhost:5001/dashboard) |

---

## 🔬 How It Works

1. **User submits a URL** via the scanner interface.
2. **Feature Extractor** parses the URL and computes 11 predictive features:
   - URL length, HTTPS status, `@` symbol presence
   - Path depth, domain length, IP-based domain check
   - Subdomain count, suspicious keyword detection
   - URL shortener detection, custom port usage, Shannon entropy
3. **Random Forest Model** predicts whether the URL is **Phishing** or **Safe**, along with a confidence probability.
4. **Result** is displayed to the user and logged to the in-memory database.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask (Python) |
| ML Model | scikit-learn (Random Forest) |
| Feature Engineering | tldextract, urllib |
| Frontend | HTML, CSS, JavaScript |
| Database | In-memory (demo mode) |

---

## 📜 License

This project is for educational and demonstration purposes.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request
