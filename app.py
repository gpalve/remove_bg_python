from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            img_io = BytesIO()
            output_image.save(img_io, 'PNG')
            img_io.seek(0)
            # Generate new filename based on original
            original_name, _ = os.path.splitext(file.filename)
            new_filename = f"{original_name}_remove_bg.png"
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=new_filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)