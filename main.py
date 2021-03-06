from flask import Flask, jsonify, request
from flask_cors import CORS
from src import success, fail, putObject, loadConfig, classifyingRubbish
from werkzeug.utils import secure_filename
import os
import json
import urllib.parse
import tinify



# 配置加载
aliAiImg = loadConfig().get('openAccessKeys').get('aliAiImg')
tinifyKey =  loadConfig().get('openAccessKeys').get('tinify').get('key')
ssoUrl = aliAiImg.get('ssoOrigin')
tinify.key = tinifyKey

IMG_EXT = ['jpg', 'jpeg', 'png']

UPLOAD_FOLDER = './source'
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 静态文件路径
uploadsDir = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploadsDir, exist_ok=True)


@app.route('/', methods=['POST'])
def uploadHandler():
    ossConnInfo = loadConfig()
    return jsonify(loadConfig())


@app.route('/file/upload', methods=['POST'])
def uploadFile():
    fds = request.files
    if not len(fds):
        return fail('上传文件为空')
    try:
        resultUrls = []
        for file in fds.values():
            fname = file.filename
            fpath = os.path.join(uploadsDir, fname)
            # 保存文件至服务器
            file.save(fpath)
            cprName = 'cpr_' + fname
            cpr_fpath = os.path.join(uploadsDir, cprName)
            tinify.from_file(fpath).to_file(cpr_fpath)
            # 上传文件至阿里云OSS
            putObject(cprName, cpr_fpath)
            fileUrl = urllib.parse.quote(ssoUrl + cprName)
            fileNameEncode = urllib.parse.quote(cprName)
            fileUrl = ssoUrl + fileNameEncode
            aiResult = classifyingRubbish(fileUrl)
            lastResp = json.loads(aiResult)
            lastResp["imgName"] = cprName
            lastResp["imgUrl"] = fileUrl
            resultUrls.append(lastResp)
        return success(resultUrls, '成功')
    except:
        return fail('失败')
