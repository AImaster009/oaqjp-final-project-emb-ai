"""
This module will send the var "textToAnalyze" to IBM AI API and return emotion
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """
    This function renders the main page of the application.
    """
    return render_template('index.html')

@app.route('/<text_to_analyze>', methods=['GET'])
def emotion_detector_name(text_to_analyze):
    """
    This function receives the text to analyze and runs emotion detection
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result_emotion_dir = emotion_detector(text_to_analyze)
    if result_emotion_dir['dominant_emotion'] is None:
        return "<strong>Invalid text! Please try again!</strong>"
    return f"""For the given statement, the system response is 'anger':
    {result_emotion_dir['anger']},'disgust': {result_emotion_dir['disgust']},
    'fear': {result_emotion_dir['fear']},'joy': {result_emotion_dir['joy']} and 'sadness': 
    {result_emotion_dir['sadness']}.The dominant emotion is 
    <strong>{result_emotion_dir['dominant_emotion']}</strong>."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
