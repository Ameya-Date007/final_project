'''
This module deal with the fetching and responding to the text provided
by the user for sentiment analysis.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emotion_analyzer():
    '''
    Retrieve the text from user and the user will evaluate
    the sentiment of the sentence, arguably the dominant
    sentiment and return the rsponse back to the user.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    ang = emotion_result['anger']
    dis = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sad = emotion_result['sadness']
    dom = emotion_result['dominant_emotion']
    if dom is None:
        return "Invalid text! Please try again!"
    return f"For input,'A':{ang},'D':{dis},'F':{fear},'J':{joy},'S':{sad}.Dominant emotion is {dom}"

@app.route('/')
def render_index_page():
    '''
    This will render the webpage where the user 
    enabled to enter the text in the textbox provided 
    and it will pass it on to emotion detection mechanism    
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 5000)
