from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup
import requests
from difflib import SequenceMatcher
import numpy as np

class Scrape():
    def __init__(self, url):
        self.url = url
        print("Processing...!!!!")
        self.domain = urlparse(self.url).netloc
        self.soup = self.fetch_website_html() 
        self.tld = self.domain.split('.')[-1]
        self._domain_length = len(self.domain)
        self._url_length = len(self.url)
        self.obfuscated_chars = ['@', '%', '&', '$', '!', '*', '(', ')', '^', '~', '#', '{', '}', '[', ']']

    def fetch_website_html(self): 
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return BeautifulSoup(response.text, 'html.parser')
            else:
                print(f"Failed to fetch URL: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def url_length(self):
        return self._url_length

    def domain_length(self):
        return self._domain_length
    
    def isDomainip(self):
        if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', self.domain):
            return True
        return 0
    
    def tld_len(self):
        tld_length = len(self.tld)
        return tld_length
    
    def no_of_subdomains(self):
        no_of_subdomains = len(self.domain.split('.')) - 2
        return no_of_subdomains
    
    def no_of_equals(self):
        no_of_equals = self.url.count('=')
        return no_of_equals
    
    def no_of_qmark(self):
        no_of_qmark = self.url.count('?')
        return no_of_qmark
    
    def no_of_ampersand(self):
        no_of_ampersand = self.url.count('&')
        return no_of_ampersand

    def no_of_special_char(self):
        self.special_char = len(re.findall(r'[^a-zA-Z0-9]', self.domain))
        return self.special_char

    def special_char_ratio(self):
        spacial_char_ratio = self.special_char / len(self.domain)
        return spacial_char_ratio
    
    def is_https(self):
        if self.url.startswith("https"):
            return 1
        return 0

    def line_of_code(self):
        if self.soup:
            return len(str(self.soup).split('\n'))
        return 0

    def largest_line_length(self):
        if self.soup:
            return max(len(line) for line in str(self.soup).split('\n'))
        return 0

    def has_title(self):
        return 1 if self.soup.title else 0

    def has_description(self):
        if self.soup:
            return 1 if self.soup.find('meta', attrs={'name': 'description'}) else 0
        return 0

    def has_password_field(self):
        if self.soup:
            return 1 if self.soup.find('input', attrs={'type': 'password'}) else 0
        return 0

    def has_favicon(self):
        if self.soup:
            return 1 if self.soup.find("link", rel=lambda rel: rel and "icon" in rel.lower()) else 0

    def no_of_css(self):
        if self.soup:
            return len(self.soup.find_all('link', {'rel': 'stylesheet'}))
        return 0

    def no_of_js(self):
        if self.soup:
            return len(self.soup.find_all('script'))
        return 0

    def no_of_popup(self):
        if self.soup:
            return len(re.findall(r'window\.open\(', str(self.soup)))
        return 0

    def has_social(self):
        social_keywords = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']
        if self.soup:
            return 1 if any(keyword in str(self.soup) for keyword in social_keywords) else 0
        return 0

    def has_copyright_info(self):
        if self.soup:
            return 1 if re.search(r'©|Copyright', str(self.soup), re.IGNORECASE) else 0
        return 0
    
    def bank(self):
        bank_keywords = ['bank', 'account', 'login', 'secure']
        if self.soup:
            url_lower = self.url.lower()
            soup_lower = str(self.soup).lower()
            url_match = any(keyword in url_lower for keyword in bank_keywords)
            soup_match = any(keyword in soup_lower for keyword in bank_keywords)
            return 1 if url_match or soup_match else 0
        return 0

    def char_continuation_rate(self):
        char_groups = re.findall(r'(\D+|\d+)', self.url) 
        if self.soup:
            if len(char_groups) > 1:
                char_continuation_rate = np.mean([len(char_groups[i])/len(char_groups[i+1]) for i in range(len(char_groups)-1)])
            else:
                char_continuation_rate = 0
        return char_continuation_rate

    def crypto(self):
        crypto_keywords = ['bitcoin', 'ethereum', 'crypto', 'wallet']
        if self.soup:
            url_lower = self.url.lower()
            soup_lower = str(self.soup).lower()
            return 1 if any(keyword in url_lower or keyword in soup_lower for keyword in crypto_keywords) else 0
        return 0

    def no_of_digits(self):
        self.no =  sum(c.isdigit() for c in self.url)
        return self.no
    
    def digit_ratio_in_url(self):
        no =  sum(c.isdigit() for c in self.url)
        return (no / len(self.url))

    def domain_title_match_score(self):
        self.title = self.soup.title.string if self.soup.title else ""
        return SequenceMatcher(None, self.domain, self.title).ratio() if self.title else 0

    def has_hidden_fields(self):
        if self.soup:
            return 1 if self.soup.find_all("input", {"type": "hidden"}) else 0

    def has_obfuscation(self):
        obfuscation_keywords = ['eval', 'atob', 'unescape', 'decode', 'fromCharCode']
        self.obfuscation = 0
        for script in self.soup.find_all("script"):
            if any(keyword in script.text.lower() for keyword in obfuscation_keywords):
                self.obfuscation = 1
                break
        return self.obfuscation

    def has_submit_button(self):
        if self.soup:
            return 1 if self.soup.find_all("input", {"type": "submit"}) or self.soup.find_all("button", {"type": "submit"}) else 0

    def has_external_form_submit(self):
        self.external_form_submit = 0
        for form in self.soup.find_all("form"):
            action = form.get("action")
            if action and not action.startswith("/") and self.url not in action:  
                self.external_form_submit = 1
                break
        return self.external_form_submit        

    def is_responsive(self):
        if self.soup:
            return 1 if self.soup.find("meta", {"name": "viewport"}) else 0

    def no_of_letters(self):
        count = sum(char.isalpha() for char in self.url)
        return count

    def letter_count_in_ratio(self):
        letter_count = sum(char.isalpha() for char in self.url)
        letter_ratio_url = letter_count / len(self.url) if len(self.url) > 0 else 0
        return letter_ratio_url

    def digit_count(self):
        return sum(char.isdigit() for char in self.url)

    def no_of_empty_ref(self):
        return len([a for a in self.soup.find_all("a") if not a.get("href")])

    def no_of_image(self):
        return len(self.soup.find_all("img"))

    def no_of_obfuscated_char(self): 
        no_of_obfuscated = sum(self.url.count(char) for char in self.obfuscated_chars)
        return no_of_obfuscated

    def no_of_external_ref(self):
        return len([a for a in self.soup.find_all("a", href=True) if self.domain not in urlparse(a['href']).netloc])

    def no_of_self_redirect(self):
        no_of_self_redirect = len([
            a for a in self.soup.find_all("a", href=True)
                if urlparse(a['href']).path == self.soup.path and
                   urlparse(a['href']).netloc == self.soup.netloc
            ])
        return no_of_self_redirect

    def no_of_self_ref(self):
        no_of_self_ref = len([
            a for a in self.soup.find_all("a", href=True)
                if urlparse(a['href']).netloc == self.soup
            ])
        return no_of_self_ref

    def no_of_redirects(self):
        meta = len(self.soup.find_all("meta", attrs={"http-equiv": "refresh"}))
        js_redirects = len([script for script in self.soup.find_all("script") if "window.location" in script.text])
        no_of_url_redirect = meta + js_redirects
        return no_of_url_redirect

    def no_of_iframe(self):
        return len(self.soup.find_all("iframe"))

    def obfuscation_ratio(self):
        no_obfuscated = sum(self.url.count(char) for char in self.obfuscated_chars)
        total_chars = len(self.url)
        if total_chars>0:
            obfuscation_ratio = (no_obfuscated / total_chars)
            return obfuscation_ratio
        return 0

    def get_tld_legitimate_prob(self):
        legitimate_tlds = {
            'com': 0.95, 'org': 0.90, 'edu': 0.95, 'gov': 0.98, 'net': 0.85,
            'mil': 0.98, 'int': 0.90, 'io': 0.85, 'co': 0.80, 'us': 0.85,
            'uk': 0.85, 'ca': 0.85, 'au': 0.85, 'de': 0.85, 'fr': 0.85
        }
        return legitimate_tlds.get(self.tld.lower(), 0.3)
    
    def calculate_url_char_prob(self):
        legitimate_freq = {
            'letters': 0.60,  
            'digits': 0.10,   
            'special': 0.30   
        }

        total_len = len(self.url)
        if total_len == 0:
            return 0

        letter_count = sum(c.isalpha() for c in self.url)
        digit_count = sum(c.isdigit() for c in self.url)
        special_count = total_len - letter_count - digit_count

        actual_freq = {
            'letters': letter_count / total_len,
            'digits': digit_count / total_len,
            'special': special_count / total_len
        }


        similarity = 1 - sum(abs(legitimate_freq[k] - actual_freq[k]) for k in legitimate_freq) / 3
        return max(0, min(1, similarity))

    def get_url_title_match_score(self):
        if not self.title:
            return 0
        domain = self.domain.split('.')[-2] if len(self.domain.split('.')) > 1 else self.domain.netloc
        cleaned_title = re.sub(r'[^a-zA-Z0-9\s]', '', self.title.lower())
        cleaned_domain = re.sub(r'[^a-zA-Z0-9\s]', '', domain.lower())
        return SequenceMatcher(None, cleaned_domain, cleaned_title).ratio()
    
    def check_payment_indicators(self):
        payment_indicators = {
            'secure_elements': [
                'ssl', 'https', 'secure', 'payment', 'checkout',
                'visa', 'mastercard', 'paypal', 'stripe'
            ],
            'security_seals': [
                'norton', 'mcafee', 'verisign', 'trustwave', 'ssl certificate'
            ]
        }

        url_text = self.url.lower()
        page_text = str(self.soup).lower()

        has_https = 1 if self.url.startswith("Https") else 0


        has_payment_keywords = any(indicator in url_text or indicator in page_text 
                                 for indicator in payment_indicators['secure_elements'])


        has_security_seals = any(seal in page_text 
                                for seal in payment_indicators['security_seals'])


        forms = self.soup.find_all('form')
        secure_forms = any(
            form.get('action', '').startswith('https://') for form in forms
        )


        indicators = [has_https, has_payment_keywords, has_security_seals, secure_forms]
        score = sum(indicators) / len(indicators)

        return 1 if score >= 0.5 else 0
    
    def check_robots_txt(self):
        try:
            robots_url = f"{self.soup.scheme}://{self.soup.netloc}/robots.txt"
            response = requests.get(robots_url, timeout=5)
            if response.status_code == 200:
                content = response.text.lower()

                good_practices = [
                    'user-agent' in content,
                    'disallow: /admin' in content or 'disallow: /wp-admin' in content,
                    'disallow: /private' in content or 'disallow: /login' in content
                ]
                return 1 if any(good_practices) else 0
            return 0
        except:
            return 0
