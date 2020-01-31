def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complete/weibo"
    # redirect_url = "https://www.baidu.com/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=2521243822, re_url=redirect_url)

    print(auth_url)


def get_access_token(code="d6eea659ca8da859cc6cdc8f25be9e44"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url,
                            data={
                                "client_id": 2521243822,
                                "client_secret": "7fc0d348161715601c8144aae7efbb25",
                                "grant_type	": "authorization_code",
                                "code": code,
                                "redirect_uri": "http://127.0.0.1:8000/complete/weibo"
                                # "redirect_uri": "https://www.baidu.com/"
                            }
                            )
    # '{"access_token":"2.00pCCk6HwgsckC64adb90f0a0F_tkr","remind_in":"157679999","expires_in":157679999,"uid":"6793309175","isRealName":"true"}'

    pass
def get_user_info(access_token="", uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=access_token, uid=uid)

    print(user_url)


if __name__ == '__main__':
    # get_auth_url()
    # get_access_token(code="d6eea659ca8da859cc6cdc8f25be9e44")
    get_user_info(access_token="2.00pCCk6HwgsckC64adb90f0a0F_tkr", uid="6793309175")

