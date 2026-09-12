"""
Emotion Detection module using IBM Watson NLP via Skills Network.
Detects: anger, disgust, fear, joy, sadness
"""
import requests
import json


def emotion_detector(text_to_analyse):
    """
    Analyze text and return emotion scores using IBM Watson NLP.
    
    Args:
        text_to_analyse: The text string to analyze
        
    Returns:
        Dictionary with emotion scores and dominant emotion
    """
    # Handle empty/invalid input
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # IBM Watson Skills Network Emotion API (free, no auth required)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        # Handle bad request (empty text, etc.)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        if response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Parse response
        result = json.loads(response.text)
        emotions = result['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion
        dominant_emotion = max(emotions, key=lambda x: emotions[x])
        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    except requests.exceptions.RequestException:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except (KeyError, IndexError, json.JSONDecodeError):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
