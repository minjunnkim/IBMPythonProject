from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('GnRt3FHzq9vdeODVN056WUzqxD5WHLEIwNCYguYW6z5D')
language_translator = LanguageTranslatorV3(
    version='2022-04-23',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/'
                                    '258d3bc8-b23a-4177-b77d-6038a9a011e8')


def english_to_french(a):
    if a is None:
        return "Invalid input, please try again"

    translation = language_translator.translate(text=a, model_id='en-fr').get_result()

    return translation['translations'][0]['translation']


def english_to_german(a):
    if a is None:
        return "Invalid input, please try again"

    translation = language_translator.translate(text=a, model_id='en-de').get_result()

    return translation['translations'][0]['translation']
