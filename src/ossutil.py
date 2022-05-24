import oss2
import os
from .config import loadConfig

aliOss = loadConfig().get('openAccessKeys').get('aliOss')
AccessKeyID = aliOss.get('keyID')
AccessKeySecret = aliOss.get('keySecret')
endPoint = aliOss.get('endPoint')
bucketName = aliOss.get('bucketName')


auth = oss2.Auth(AccessKeyID, AccessKeySecret)
bucket = oss2.Bucket(auth, endPoint, bucketName)


# 必须以二进制的方式打开文件。
# 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
# print(os.path.join(os.getcwd(), 'uploads', 'ffmpeg.dll'))
# path = os.path.join(os.getcwd(), 'uploads', 'ffmpeg.dll')
# bucket.put_object_from_file('exampleobject.txt', path)
def putObject(filename, filePath):
    try:
        bucket.put_object_from_file(filename, filePath)
        return filename
    except:
        return -1
