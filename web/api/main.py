import os
import copy
import datetime
from flask import Flask, request, json, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('..', 'data')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


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
    filename = secure_filename(file.filename)
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
      filename_first_part = filename[:filename.rfind('.')]
      filename_second_part = filename[filename.rfind('.'):len(filename)]
      filename = filename_first_part + '.' + str(datetime.datetime.now()) + filename_second_part
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    resp = Response(json.dumps({'car_type': 'Audi A6'}))
    resp.headers['Content-Type'] = 'application/json'
    return resp
  resp = Response(json.dumps({'error': 'There was error processing your request'}))
  resp.headers['Content-Type'] = 'application/json'
  resp.status_code = 400
  return resp

if __name__ == '__main__':
  app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  app.config['SECRET_KEY'] = 'cars123'
  app.run()
