import re
from urllib.parse import urlparse
import tldextract
import math

class FeatureExtractor:
    def __init__(self):
        self.suspicious_words = ['login', 'verify', 'update', 'secure', 'bank', 'account', 'auth', 'confirm', 'free', 'wallet']
        self.shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd', 'buff.ly', 'cutt.ly']

    def _calculate_entropy(self, text):
        if not text:
            return 0
        entropy = 0
        for x in set(text):
            p_x = float(text.count(x)) / len(text)
            entropy += - p_x * math.log(p_x, 2)
        return entropy

    def extract_features(self, url: str) -> list:
        try:
            parsed_url = urlparse(url)
            ext = tldextract.extract(url)
            
            length_url = len(url)
            has_https = 1 if parsed_url.scheme == 'https' else 0
            has_at_symbol = 1 if '@' in url else 0
            path_depth = len(list(filter(None, parsed_url.path.split('/'))))
            domain_length = len(ext.domain)
            has_ip = 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ext.domain) else 0

            # 5 New Predictive Security Features
            num_subdomains = len(list(filter(None, ext.subdomain.split('.')))) if ext.subdomain else 0
            has_suspicious_words = 1 if any(word in url.lower() for word in self.suspicious_words) else 0
            
            domain_suffix = ext.domain + ('.' + ext.suffix if ext.suffix else '')
            is_shortened = 1 if domain_suffix in self.shorteners else 0
            
            has_port = 1 if parsed_url.port else 0
            entropy = round(self._calculate_entropy(url), 2)

            return [
                length_url, has_https, has_at_symbol, path_depth, domain_length, 
                has_ip, num_subdomains, has_suspicious_words, is_shortened, has_port, entropy
            ]
            
        except Exception as e:
            raise ValueError(f"Failed to extract features from URL: {str(e)}")