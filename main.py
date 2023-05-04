from flask import Flask, render_template, request
from chat import get_response
app = Flask(__name__)

# Define a global variable to store the transcription
transcription = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    global transcription
    if request.method == 'POST':
        if 'stop-button' in request.form:
            result = transcription
            transcription = ""
            return result
        else:
            transcription += request.form['transcription']
        print(transcription)
        print(get_response(transcription))
    return render_template("SpeechToText.html")


app.run()