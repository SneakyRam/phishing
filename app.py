from flask import Flask, request, jsonify, render_template
from feature_extractor import FeatureExtractor
from model_handler import PhishingDetectorModel
from db_handler import DatabaseHandler
import urllib.parse

app = Flask(__name__)

# Initialize modules
extractor = FeatureExtractor()
detector = PhishingDetectorModel()
db = DatabaseHandler()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/scanner')
def scanner():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    data = db.get_dashboard_data()
    return render_template('dashboard.html', dashboard_data=data)

@app.route('/analyze', methods=['POST'])
def analyze_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400

    raw_url = data['url'].strip()

    # Basic input validation
    if not raw_url.startswith(('http://', 'https://')):
        raw_url = 'http://' + raw_url

    try:
        # 1. Parse and extract features
        features = extractor.extract_features(raw_url)

        # 2. Predict using ML Model
        threat_status, probability = detector.predict(features)

        # 3. Log to Database
        db.log_scan(raw_url, threat_status, features, probability=probability)

        # 4. Return to Frontend
        return jsonify({
            "url": raw_url,
            "status": threat_status,
            "probability": probability,
            "features_analyzed": features
        }), 200

    except ValueError as ve:
        return jsonify({"error": f"Invalid URL structure: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
