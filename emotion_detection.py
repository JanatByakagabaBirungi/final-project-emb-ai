import requests

def emotion_detector(text_to_analyse):
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Format the input text into a dictionary as expected by the API
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the text attribute of the response
    return response.text