"""
This is a module for performing emotion detection on the text.
"""

import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyse: str):
    """
    Analyzes text using Watson NLP
    """
    # Send request
    json_body = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=json_body, headers=HEADERS)

    # Format to JSON and get data
    response_json = json.loads(response)
    emotion_scores = response_json["emotionPredictions"][0]["emotion"]
    anger_score = emotion_scores["anger"]
    disgust_score = emotion_scores["disgust"]
    fear_score = emotion_scores["fear"]
    joy_score = emotion_scores["joy"]
    sadness_score = emotion_scores["sadness"]

    dominant_emotion = ""
    best_score = -float('inf')
    for emotion, score in emotion_scores.items():
        if score > best_score:
            best_score = score
            dominant_emotion = emotion

    # Format output
    payload = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }

    return payload
