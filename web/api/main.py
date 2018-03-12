import os
import uuid

from flask import Flask, request, jsonify

from web.api.exceptions import HTTPException, HTTPBadRequest, HTTPPayloadTooLarge, HTTPMessage
from machine_learning.inception import checkpoint_model_api
from web.model.model import *
#from web.model.model import Company

app = Flask(__name__)


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# Log directory where checkpoint model is saved


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
        predict_label_id = app.config['MODEL'].predict(image_path=file_path)
        full_model = FullModel.get_full_model(app=app, id_label=predict_label_id)
        return jsonify({'car_company': full_model.Company.Name,
                        'car_model': full_model.Model.Name,
                        'car_chassis': full_model.Version.Name})
    else:
        raise HTTPBadRequest(HTTPMessage.NOT_EXTENSION_ALLOWED)


def init_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Baba1234*@localhost:5432/db_cars'
    with app.app_context():
        db.init_app(app)
    delete_data(app)
    create_data(app)
if __name__ == '__main__':
    init_database()
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), '..\data')
    app.config['SECRET_KEY'] = 'cars123'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    log_dir = os.path.join(os.getcwd(), '..\..\log');
    app.config['MODEL'] = checkpoint_model_api.ConvNetModel(checkpoint_dir=log_dir)

    app.run('10.0.0.220', 5000);
