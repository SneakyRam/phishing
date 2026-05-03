import datetime
from datetime import datetime, timezone

class DatabaseHandler:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="phishing_db"):
        self.logs = []
        print("Using in-memory dummy database for presentation.")

    def log_scan(self, url: str, status: str, features: list, probability: float = 0.0):
        """Logs the URL, prediction status, and extracted features."""
        try:
            log_entry = {
                "url": url,
                "status": status,
                "features_extracted": features,
                "probability": probability,
                "timestamp": datetime.now(timezone.utc)
            }
            self.logs.insert(0, log_entry)  # Add to beginning
            return True
        except Exception as e:
            print(f"Failed to insert log: {str(e)}")
            return False

    def get_dashboard_data(self):
        """Fetches summary data for the dashboard."""
        try:
            if len(self.logs) == 0:
                dummy_data = [
                    {"url": "http://secure-login-paypal.com/auth", "status": "Phishing", "probability": 0.98, "timestamp": datetime.now(timezone.utc)},
                    {"url": "https://www.github.com", "status": "Safe", "probability": 0.99, "timestamp": datetime.now(timezone.utc)},
                    {"url": "http://192.168.1.100/verify_account", "status": "Phishing", "probability": 0.89, "timestamp": datetime.now(timezone.utc)},
                    {"url": "https://mybank.com", "status": "Safe", "probability": 0.95, "timestamp": datetime.now(timezone.utc)}
                ]
                self.logs.extend(dummy_data)

            total_scans = len(self.logs)
            phishing_count = sum(1 for log in self.logs if log['status'].lower() == 'phishing')
            safe_count = total_scans - phishing_count
            recent_scans = self.logs[:10]

            return {
                "total_scans": total_scans,
                "phishing_count": phishing_count,
                "safe_count": safe_count,
                "recent_scans": recent_scans
            }
        except Exception as e:
            print(f"Failed to fetch dashboard data: {str(e)}")
            return {"total_scans": 0, "phishing_count": 0, "safe_count": 0, "recent_scans": []}
