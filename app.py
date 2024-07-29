from flask import Flask, render_template, request, jsonify
from transformers import VisionEncoderDecoderModel, AutoTokenizer, ViTImageProcessor, BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import torch
import base64
import io

app = Flask(__name__)

model_2 = 'C:/Users/vivek/OneDrive/Desktop/Image Caption Generator/models/Model 2'

processor = BlipProcessor.from_pretrained(model_2)
model2 = BlipForConditionalGeneration.from_pretrained(model_2)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables
    image_display = None
    caption1 = None
    error_message = None

    if request.method == 'POST':
        try:
            if 'file' in request.files:
                file = request.files['file']
                if file:
                    img = Image.open(file)
                    image_display = convert_image_to_base64(img)

            elif 'sample_image' in request.form:
                img_name = request.form['sample_image']
                img_path = f'static/images/{img_name}.jpg'
                img = Image.open(img_path)
                image_display = convert_image_to_base64(img)

            elif 'random_image' in request.form:
                img_url = 'https://source.unsplash.com/random'
                img = Image.open(requests.get(img_url, stream=True).raw)
                image_display = convert_image_to_base64(img)
        except Exception as e:
            error_message = str(e)

    return render_template('index.html', image=image_display, caption1=caption1, error_message=error_message)

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    image = request.form['image_base64']
    img = Image.open(io.BytesIO(base64.b64decode(image.split(',')[1])))
    #caption1 = predict_caption_1(img)
    caption2 = predict_caption_2(img)
    return render_template('index.html', image=image, caption2=caption2)

def convert_image_to_base64(img):
    img = img.convert("RGB")
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return f"data:image/jpeg;base64,{img_str.decode('utf-8')}"

def predict_caption_2(image):
    inputs = processor(image, return_tensors="pt")
    out = model2.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

if __name__ == "__main__":
    app.run(debug=True)
