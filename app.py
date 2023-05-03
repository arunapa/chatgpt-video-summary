from flask import Flask, render_template, request
import os
import utils

app = Flask(__name__)

@app.route('/')
def home():
    transcript = utils.get_transcript()
    result = utils.get_response_from_chatgpt(utils.construct_prompt(transcript=transcript))
    return render_template('index.html', result=result, transcript=transcript)

@app.route('/upload', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_data = f.read().decode('utf-8')
        result = utils.get_response_from_chatgpt(utils.construct_prompt(transcript=file_data))
        return render_template('index.html', result=result, transcript=file_data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)