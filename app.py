from flask import Flask, render_template, request
import os
import utils

app = Flask(__name__)

@app.route('/')
def home():
    transcript = utils.get_transcript()
    one_line_summary = utils.get_response_from_chatgpt(utils.one_line_summary(transcript=transcript))
    shorter_1 = utils.get_response_from_chatgpt(utils.make_shorter(transcript=one_line_summary))
    shorter_2 = utils.get_response_from_chatgpt(utils.make_shorter(transcript=shorter_1))
    return render_template(
        'index.html',
        result=one_line_summary,
        transcript=transcript,
        shorter_1=shorter_1,
        shorter_2=shorter_2
    )

@app.route('/upload', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_data = f.read().decode('utf-8')
        one_line_summary = utils.get_response_from_chatgpt(utils.one_line_summary(transcript=file_data))
        shorter_1 = utils.get_response_from_chatgpt(utils.make_shorter(transcript=one_line_summary))
        shorter_2 = utils.get_response_from_chatgpt(utils.make_shorter(transcript=shorter_1))
        return render_template(
            'index.html',
            result=one_line_summary,
            transcript=file_data,
            shorter_1=shorter_1,
            shorter_2=shorter_2
        )
        return render_template('index.html', result=result, transcript=file_data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)