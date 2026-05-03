import os
import pickle
import numpy as np

class PhishingDetectorModel:
    def __init__(self, model_path='models/phishing_model.pkl'):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        """Loads a pre-trained scikit-learn model."""
        try:
            # For demonstration, returning a mock predictor if file doesn't exist
            if not os.path.exists(self.model_path):
                print("Warning: Model file not found. Using mock prediction logic.")
                return None
            
            with open(self.model_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load ML model: {str(e)}")

    def predict(self, features: list) -> tuple:
        """
        Takes extracted features and returns a tuple of ('Phishing' or 'Safe', confidence_probability).
        """
        if self.model is None:
            # Mock logic: If domain length > 15 or contains IP, flag as phishing
            is_phishing = features[4] > 15 or features[5] == 1
            return ("Phishing", 0.85) if is_phishing else ("Safe", 0.92)

        try:
            # Reshape for sklearn/tf prediction
            features_array = np.array(features).reshape(1, -1)
            prediction = self.model.predict(features_array)[0]
            probability = self.model.predict_proba(features_array)[0]
            max_prob = max(probability)
            
            # Assuming 1 = Phishing, 0 = Safe
            return ("Phishing", float(max_prob)) if prediction == 1 else ("Safe", float(max_prob))
        except Exception as e:
            raise RuntimeError(f"Prediction failed: {str(e)}")
