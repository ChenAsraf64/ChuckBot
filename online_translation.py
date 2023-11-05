import requests
import uuid
import os

key = os.getenv('AZURE_TRANSLATOR_KEY')
endpoint = os.getenv('AZURE_TRANSLATOR_ENDPOINT')
location = os.getenv('AZURE_TRANSLATOR_LOCATION')

# Given language name in English, extracting the language code


def get_language_code(language_name):
    # Define the endpoint URL to get the supported languages
    url = f"{endpoint}/languages?api-version=3.0&scope=translation"

    # Set up the headers with your subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-Type': 'application/json'
    }
    # Make a GET request to the endpoint
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        languages = response.json().get('translation', {})
        # Search for the language code by name
        for code, details in languages.items():
            if language_name.lower() in details['name'].lower():
                return code  # Return the language code
    # If the language name was not found or the request failed
    return None


# Translation text based on language that was choosen
def get_translation(language_code, text_to_translate):
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': language_code  # the languge that choose for language translate
    }
    body = [{
        'text': text_to_translate
    }]

    if language_code:
        params['to'] = language_code
    else:
        # Need to retun that throw the bot
        print('Language not found or failed to retrieve languages.')
        return

    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    request = requests.post(constructed_url, params=params,
                            headers=headers, json=body)
    response = request.json()
    translated_text = response[0]['translations'][0]['text']
    return translated_text
