import json
import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"
    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【田帅】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        # print(re_dict)
        return re_dict
if __name__ == "__main__":
    yun_pian = YunPian("7146d20a2c491f615894d8a687445a55")
    yun_pian.send_sms("6598", "13753643834")