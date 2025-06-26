from flask import Flask, request, jsonify
import joblib
import pandas as pd
from urllib.parse import urlparse
from Model.extract import Scrape

with open(r"D:\Projects\Phishing-Domains-Detection\Model\SGD_model.joblib", 'rb') as f:
    model = joblib.load(f)

with open(r"D:\Projects\Phishing-Domains-Detection\Model\scaler.pkl", 'rb') as f:
    scaler = joblib.load(f)

app = Flask(__name__)

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

def extract_features(fetch):
    features = {
        'URLLength': fetch.url_length(),
        'DomainLength': fetch.domain_length(),
        'IsDomainIP': fetch.isDomainip(),
        'CharContinuationRate': fetch.char_continuation_rate(),
        'TLDLegitimateProb': fetch.get_tld_legitimate_prob(),
        'URLCharProb': fetch.calculate_url_char_prob(),
        'TLDLength': fetch.tld_len(),
        'NoOfSubDomain': fetch.no_of_subdomains(),
        'HasObfuscation': fetch.has_obfuscation(),
        'NoOfObfuscatedChar': fetch.no_of_obfuscated_char(),
        'ObfuscationRatio': fetch.obfuscation_ratio(),
        'NoOfLettersInURL': fetch.no_of_letters(),
        'LetterRatioInURL': fetch.letter_count_in_ratio(),
        'NoOfDegitsInURL': fetch.digit_count(),
        'DegitRatioInURL': fetch.digit_ratio_in_url(),
        'NoOfEqualsInURL': fetch.no_of_equals(),
        'NoOfQMarkInURL': fetch.no_of_qmark(),
        'NoOfAmpersandInURL': fetch.no_of_ampersand(),
        'NoOfOtherSpecialCharsInURL': fetch.no_of_special_char(),
        'SpacialCharRatioInURL': fetch.special_char_ratio(),
        'IsHTTPS': fetch.is_https(),
        'LineOfCode': fetch.line_of_code(),
        'LargestLineLength': fetch.largest_line_length(),
        'HasTitle': fetch.has_title(),
        'DomainTitleMatchScore': fetch.domain_title_match_score(),
        'URLTitleMatchScore': fetch.get_url_title_match_score(),
        'HasFavicon': fetch.has_favicon(),
        'Robots': fetch.check_robots_txt(),
        'IsResponsive': fetch.is_responsive(),
        'NoOfURLRedirect': fetch.no_of_redirects(),
        'NoOfSelfRedirect': fetch.no_of_self_redirect(),
        'HasDescription': fetch.has_description(),
        'NoOfPopup': fetch.no_of_popup(),
        'NoOfiFrame': fetch.no_of_iframe(),
        'HasExternalFormSubmit': fetch.has_external_form_submit(),
        'HasSocialNet': fetch.has_social(),
        'HasSubmitButton': fetch.has_submit_button(),
        'HasHiddenFields': fetch.has_hidden_fields(),
        'HasPasswordField': fetch.has_password_field(),
        'Bank': fetch.bank(),
        'Pay': fetch.check_payment_indicators(),
        'Crypto': fetch.crypto(),
        'HasCopyrightInfo': fetch.has_copyright_info(),
        'NoOfImage': fetch.no_of_image(),
        'NoOfCSS': fetch.no_of_css(),
        'NoOfJS': fetch.no_of_js(),
        'NoOfSelfRef': fetch.no_of_self_ref(),
        'NoOfEmptyRef': fetch.no_of_empty_ref(),
        'NoOfExternalRef': fetch.no_of_external_ref()
    }

    feature_order = [
        'URLLength', 'DomainLength', 'IsDomainIP', 'CharContinuationRate', 'TLDLegitimateProb', 'URLCharProb', 
        'TLDLength', 'NoOfSubDomain', 'HasObfuscation', 'NoOfObfuscatedChar', 'ObfuscationRatio', 'NoOfLettersInURL', 
        'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL', 'NoOfEqualsInURL', 'NoOfQMarkInURL', 
        'NoOfAmpersandInURL', 'NoOfOtherSpecialCharsInURL', 'SpacialCharRatioInURL', 'IsHTTPS', 'LineOfCode', 
        'LargestLineLength', 'HasTitle', 'DomainTitleMatchScore', 'URLTitleMatchScore', 'HasFavicon', 'Robots', 
        'IsResponsive', 'NoOfURLRedirect', 'NoOfSelfRedirect', 'HasDescription', 'NoOfPopup', 'NoOfiFrame', 
        'HasExternalFormSubmit', 'HasSocialNet', 'HasSubmitButton', 'HasHiddenFields', 'HasPasswordField', 'Bank', 
        'Pay', 'Crypto', 'HasCopyrightInfo', 'NoOfImage', 'NoOfCSS', 'NoOfJS', 'NoOfSelfRef', 'NoOfEmptyRef', 
        'NoOfExternalRef'
    ]

    return pd.DataFrame([features], columns=feature_order)

@app.route('/predict', methods=['POST'])
def predict_phishing():
    data = request.json.get('url') if request.is_json else request.form.get('url')

    try:
        fetch = Scrape(data)
        features = extract_features(fetch)
        print(features)

        scaled_input = scaler.transform(features)
        prediction = model.predict(scaled_input)
        result = 0 if prediction[0] == 1 else 1
        return jsonify({"prediction": result})
    except Exception as e:
        print(f"Error during scraping or prediction: {e}")
        return jsonify({"prediction": 1}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


