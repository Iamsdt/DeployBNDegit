import base64
import os
import sys
import torch
from flask import Flask, render_template, request
from Loader import load

sys.path.append(os.path.abspath('model'))
sys.path.append(os.path.abspath('templates'))

# init flask app
app = Flask(__name__, template_folder='templates')

global model

model = load.init()


def convert_image(x):
    x = x.replace('data:image/png;base64,'.encode(), ''.encode())
    with open("output.png", "wb") as fh:
        fh.write(base64.decodebytes(x))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    imdata = request.get_data()
    convert_image(imdata)
    x = load.transform('output.png')
    with torch.no_grad():
        out = model(x)
        proba = torch.exp(out)
        top_p, top_class = proba.topk(1, dim=1)
        value = top_class.item()
        return str(value)


if __name__ == "__main__":
    app.run()
