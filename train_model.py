import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

np.random.seed(42)
random.seed(42)

X = []
y = []

# Generate 3000 synthetic samples to make the Machine Learning model highly predictive
# Features: [length_url, has_https, has_at_symbol, path_depth, domain_length, has_ip, 
#            num_subdomains, has_suspicious_words, is_shortened, has_port, entropy]

for _ in range(3000):
    is_phishing = random.choice([0, 1])
    
    if is_phishing:
        # Advanced Phishing Indicators
        has_https = random.choices([0, 1], weights=[0.8, 0.2])[0]
        has_at_symbol = random.choices([0, 1], weights=[0.6, 0.4])[0] 
        has_ip = random.choices([0, 1], weights=[0.7, 0.3])[0]
        
        num_subdomains = random.randint(1, 5) # Phishers spoof companies via subdomains
        has_suspicious_words = random.choices([0, 1], weights=[0.2, 0.8])[0] # Highly likely to contain 'login', etc
        is_shortened = random.choices([0, 1], weights=[0.7, 0.3])[0] 
        has_port = random.choices([0, 1], weights=[0.8, 0.2])[0] # Custom attacking ports
        entropy = random.uniform(4.5, 6.5) # Disordered, random URLs have higher entropy
        
        path_depth = random.randint(3, 10)
        domain_length = random.randint(15, 60)
        
        if has_ip:
            domain_length = random.randint(11, 15)
            
        length_url = domain_length + (path_depth * random.randint(6, 18)) + random.randint(10, 25)
        
    else:
        # Standard Enterprise Safe URL Profiles
        has_https = random.choices([0, 1], weights=[0.05, 0.95])[0] 
        has_at_symbol = random.choices([0, 1], weights=[0.99, 0.01])[0] 
        has_ip = random.choices([0, 1], weights=[0.99, 0.01])[0]
        
        num_subdomains = random.choices([0, 1, 2], weights=[0.6, 0.3, 0.1])[0]
        has_suspicious_words = random.choices([0, 1], weights=[0.95, 0.05])[0]
        is_shortened = random.choices([0, 1], weights=[0.9, 0.1])[0]
        has_port = random.choices([0, 1], weights=[0.95, 0.05])[0]
        entropy = random.uniform(3.0, 4.5) 
        
        path_depth = random.randint(0, 3)
        domain_length = random.randint(5, 20)
        
        length_url = domain_length + (path_depth * random.randint(3, 10)) + random.randint(8, 15)

    X.append([length_url, has_https, has_at_symbol, path_depth, domain_length, has_ip, num_subdomains, has_suspicious_words, is_shortened, has_port, entropy])
    y.append(is_phishing)

X = np.array(X)
y = np.array(y)

# Train an Enterprise-Grade Random Forest Model. Deeper tree to account for 11 distinct attack vectors. 
clf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
clf.fit(X, y)

model_path = 'models/phishing_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(clf, f)

print("Enterprise Analytics Model (11 Features) successfully trained on 3,000 synthesized instances and saved!")