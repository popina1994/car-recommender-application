import os
import uuid

from flask import Flask, request, jsonify

from exceptions import HTTPException, HTTPBadRequest, HTTPPayloadTooLarge, HTTPMessage
from machine_learning.inception import checkpoint_model_api

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Log directory where checkpoint model is saved
log_dir = os.path.join('log')

# Labels path
labels_path = os.path.join(log_dir, 'labels.txt')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.errorhandler(HTTPException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.errorhandler(413)
def error413(_):
    response = jsonify(HTTPPayloadTooLarge(HTTPMessage.FILE_IS_TOO_LARGE).to_dict())
    response.status_code = 413
    return response

@app.route("/v1/rpc/upload", methods=['POST'])
def upload_image():
    # check if the post request has the file part
    if 'file' not in request.files or request.files['file'].filename == '':
        raise HTTPBadRequest(HTTPMessage.MISSING_FILE_PART)
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4().hex) + '.' + file.filename.rsplit('.', 1)[1].lower()
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        predict = app.config['MODEL'].predict(image_path=file_path)
        return jsonify({'car_type': str(predict)})
    else:
        raise HTTPBadRequest(HTTPMessage.NOT_EXTENSION_ALLOWED)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'web', 'data')
    app.config['SECRET_KEY'] = 'cars123'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['MODEL'] = checkpoint_model_api.ConvNetModel(checkpoint_dir=log_dir, labels_path=labels_path)
    app.run()
