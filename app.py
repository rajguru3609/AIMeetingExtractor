from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from whisper_utils import transcribe_audio
from gpt_utils import analyze_meeting
app=Flask(__name__)
CORS(app)
UPLOAD_FOLDER='uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    transcript = transcribe_audio(filepath)
    result = analyze_meeting(transcript)

    return jsonify({
        "transcript": transcript,
        "analysis": result
    })


if __name__ == '__main__':
    app.run(debug=True)