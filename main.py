from flask import Flask, jsonify, request
from src import success, fail
from werkzeug.utils import secure_filename
import os

IMG_EXT = ['jpg', 'jpeg', 'png']

# def formatFileName():
# ErrorMsg = {
#     FileNotFound: "你没有上传文件"
# }

# 保存文件
uploads_dir = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

# 保存文件
def saveFileToServer(file):
    file.save(os.path.join(app.config['UPLOAD_FOLDER']), 'test')

UPLOAD_FOLDER = './source'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/upload', methods=['POST'])
def uploadHandler():
    return jsonify([{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}])

@app.route('/file/upload', methods=['POST'])
def uploadFile():
    # print(request.files)
    fds = request.files
    if not len(fds):
        return fail('失败')
    for fKey in fds.values():
        fKey.save(os.path.join(uploads_dir), secure_filename('test'))
    return success({'success': True}, '成功')
