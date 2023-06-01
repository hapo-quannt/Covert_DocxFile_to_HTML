from flask import Flask, request, jsonify
from load import convert_docx_to_html_file
from removeFile import delete_old_file
from getContent import extract_body_content
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['post'])
def convert_word_to_html():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})
    file = request.files['file']
    file_path = file.filename

    file.save(file_path)

    output_file = "output.html"

    delete_old_file(output_file)

    convert_docx_to_html_file(file_path, output_file)

    response = extract_body_content(output_file)

    os.remove(file_path)

    return response


if __name__ == '__main__':
    app.run()
