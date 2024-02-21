import os
import requests
import base64
path = 'test/文字验证码'


def xiaridenuanfeng_Tools(file):

    length = len(os.path.splitext(os.path.basename(file))[0])
    base64_data = base64.b64encode(open(file, 'rb').read()).decode("utf8")
    r = requests.get(
        f'http://127.0.0.1:8888/aqwj/?code={base64_data}&length={length}')
    print(os.path.basename(file), r.text)


for file in os.listdir(path):
    full_file = os.path.join(path, file)
    xiaridenuanfeng_Tools(full_file)
