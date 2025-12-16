from flask import Flask, render_template, request
import os
from colorize_utils import colorize_image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    original_image = None
    colorized_image = None

    if request.method == 'POST':
        file = request.files['image']

        if file.filename != '':
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            output_path = os.path.join(RESULT_FOLDER, file.filename)

            file.save(input_path)
            colorize_image(input_path, output_path)

            original_image = input_path
            colorized_image = output_path

    return render_template(
        'index.html',
        original_image=original_image,
        colorized_image=colorized_image
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)
