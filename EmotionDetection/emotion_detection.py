import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    dominant_emotion = formatted_response['emotionPredictions'][0]['emotion']
    biggest_value_emotion = max(dominant_emotion, key=dominant_emotion.get)
    dominant_emotion['dominant_emotion'] = biggest_value_emotion
    return dominant_emotion

"""
python3.11
from emotion_detection import emotion_detector
emotion_detector("I am so happy I am doing this.")
"""