import requests
import json


class setuPic:
    pid = '0'
    title = 'Null'
    author = 'Null'
    tags = 'Null'
    url = 'https://'

    def __init__(self, p, a, t, tags, u):
        self.pid = p
        self.url = u
        self.title = t
        self.author = a
        self.tags = tags


def list2str(contentList):
    """将数组转换为文本"""
    text = ''
    for i in range(len(contentList)):
        if i == 0:
            text = text + contentList[i]
        text = text + " " + contentList[i]
    return text


def getSetuUrl():
    try:
        js = json.loads(requests.get('https://api.lolicon.app/setu/v2').text)
        url = js['data'][0]['urls']['original']
        pid = js['data'][0]['pid']
        author = js['data'][0]['author']
        title = js['data'][0]['title']
        tags = js['data'][0]['tags']
        setu = setuPic(pid, author, title, list2str(tags), url)
        print('获取涩图 => ' + url)
        return setu
    except Exception as e:
        print(f'获取图片失败=> {e}')
        return '-1'
