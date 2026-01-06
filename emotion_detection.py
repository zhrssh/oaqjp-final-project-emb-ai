"""
This is a module for performing emotion detection on the text.
"""

import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse: str):
    """
    Analyzes text using Watson NLP
    """
    json_body = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=json_body, headers=HEADERS)

    return response.text
