from flask import Flask, render_template, request, jsonify, send_file
import whisper
from gtts import gTTS
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper model once
model = whisper.load_model("base")

@app.route('/')
def home():
    return render_template('frontend.html')


# Voice → Text
@app.route('/speech_to_text', methods=['POST'])
def speech_to_text():

    audio = request.files['audio']

    filepath = os.path.join(
        UPLOAD_FOLDER,
        audio.filename
    )

    audio.save(filepath)

    result = model.transcribe(filepath)

    return jsonify({
        "text": result["text"]
    })


# Text → Voice
@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():

    text = request.form['text']
    lang = request.form['lang']

    tts = gTTS(
        text=text,
        lang=lang
    )

    output = os.path.join(
        UPLOAD_FOLDER,
        "output.mp3"
    )

    tts.save(output)

    return send_file(
        output,
        as_attachment=False
    )


import webbrowser

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)