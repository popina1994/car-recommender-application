import os
import uuid
from flask import Flask, request, json, Response
from werkzeug.utils import secure_filename
from machine_learning.inception import checkpoint_model_api

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('data')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Log directory where checkpoint model is saved
log_dir = os.path.join('log')

# Labels path
labels_path = os.path.join(log_dir, 'labels.txt')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/v1/rpc/upload", methods=['POST'])
def upload_image():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = Response(json.dumps({'error': 'There is no file part'}))
        resp.headers['Content-Type'] = 'application/json'
        resp.status_code = 400
        return resp
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        resp = Response(json.dumps({'error': 'There is no file'}))
        resp.headers['Content-Type'] = 'application/json'
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4().hex) + '.' + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(os.getcwd(), 'web', app.config['UPLOAD_FOLDER'], filename))
        pred = app.config['MODEL'].predict(image_path=os.path.join(os.getcwd(), 'web', app.config['UPLOAD_FOLDER'], filename))
        resp = Response(json.dumps({'car_type': str(pred)}))
        resp.headers['Content-Type'] = 'application/json'
        return resp
    resp = Response(json.dumps({'error': 'There was error processing your request'}))
    resp.headers['Content-Type'] = 'application/json'
    resp.status_code = 400
    return resp


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'cars123'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['MODEL'] = checkpoint_model_api.ConvNetModel(checkpoint_dir=log_dir, labels_path=labels_path)
    app.run()
