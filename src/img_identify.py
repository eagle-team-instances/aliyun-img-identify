from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkimagerecog.request.v20190930.ClassifyingRubbishRequest import ClassifyingRubbishRequest

from .config import loadConfig

root = loadConfig().get('openAccessKeys').get('aliAiImg')
AccessKeyID = root.get('keyID')
AccessKeySecret = root.get('keySecret')
credentials = AccessKeyCredential(AccessKeyID, AccessKeySecret)
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>')
client = AcsClient(region_id='cn-shanghai', credential=credentials)
request = ClassifyingRubbishRequest()
request.set_accept_format('json')

def classifyingRubbish(ossImgUrl):
    request.add_body_params('ImageURL', ossImgUrl)

    response = client.do_action_with_exception(request)
    return str(response, encoding='utf-8')
