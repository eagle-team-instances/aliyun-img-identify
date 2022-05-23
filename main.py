from flask import Flask, jsonify, request
from src import success, fail
from werkzeug.utils import secure_filename
import os

IMG_EXT = ['jpg', 'jpeg', 'png']

UPLOAD_FOLDER = './source'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 静态文件路径
uploads_dir = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/upload', methods=['POST'])
def uploadHandler():
    return jsonify([{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}])


@app.route('/file/upload', methods=['POST'])
def uploadFile():
    # print(request.files)
    fds = request.files
    if not len(fds):
        return fail('失败')
    for file in fds.values():
        file.save(os.path.join(uploads_dir, file.filename))
    return success({'success': True}, '成功')
