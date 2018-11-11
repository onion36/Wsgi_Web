import json
from .web import  MageWeb




#json化
def jsonify(**kwargs):
    content = json.dumps(kwargs)
    return MageWeb.Response(content, '200 ok', content_type='application/json', charset='utf-8')










