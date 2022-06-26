import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


# by suleiman abdulkadir
def english_to_french(english_text):
    """Translates English to French"""
    frenchtranslation = language_translator.translate(text=english_text,
                                                      model_id='en-fr').get_result()
    # return frenchtranslation.get("translations")[0].get("translate")
    return frenchtranslation["translations"][0]["translation"].lower()

# by suleiman abdulkadir
def french_to_english(french_text):
    """Transalates French to English"""
    englishtranslation = language_translator.translate(text=french_text,
                                                       model_id='fr-en').get_result()
    return englishtranslation["translations"][0]["translation"].lower()


# print(english_to_french('apple'))
# print(french_to_english('bon'))
