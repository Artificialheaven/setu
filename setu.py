import requests
import json

def getSetuUrl():
    try:
        js = json.loads(requests.get('https://api.lolicon.app/setu/v2').text)
        url = js['data'][0]['urls']['original']
        print('获取涩图 => ' + url)
        return url
    except Exception as e:
        print('获取图片失败=> ' + e)
    else:
        print('尝试获取涩图成功√')

def sendSetuG(group_id, send):
    try:
        send(group_id, '[CQ:image,file=' + getSetuUrl() + ",c=8]")
        return
    except Exception as e:
        print('发送涩图失败=> ' + e)
    else:
        print('发送涩图成功=> ' + group_id)

def sendSetuP(user_id, sender):
    try:
        sender(user_id, '[CQ:image,file=' + getSetuUrl() + ",c=8]")
        return
    except Exception as e:
        print('发送涩图失败=> ' + e)
    else:
        print('发送涩图成功=> ' + user_id)
