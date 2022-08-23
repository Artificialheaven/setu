import asyncio
import configparser
import os
import sys

import Bot
import Listener


def receivegroupmsg(group_id, user_id, msg):
    """收到群消息，group_id为群号，user_id为发送人，msg为消息内容"""
    Listener.recG(group_id, user_id, msg, Bot.sendGroupMsg)
    return


def receiveprivatemsg(user_id, msg):
    """收到私聊消息，user_id为发送人，msg为消息内容"""
    Listener.recP(user_id, msg, Bot.sendPrivateMsg)
    return


Plugins_name = 'setu'
#   插件名
Plugins_info = ''
#   初始化配置
config = configparser.ConfigParser()

if os.path.isfile('./config.ini'):
    #   文件存在。
    config.read('./config.ini')
    ip = config['Bot']['ip']
    hp = config['Bot']['hp']
    wp = config['Bot']['wp']
else:
    #   文件不存在，创建并提示要求修改该文件。
    #   file = open('./config.ini','w')
    #   file.close()
    config['Bot'] = {
        'ip' : '127.0.0.1',
        'hp' : '5700',
        'wp' : '8888'
    }
    with open('./config.ini', 'w') as configfile:
        config.write(configfile)
    print('未检测到配置文件，已生成于 ./config.ini 请修改后重启本程序。')
    sys.exit()
try:
    os.mkdir(f'./{Plugins_name}/')
except Exception as e:
    print(f'error=> {e}')
finally:
    print('应用目录已生成于=> %s' % (sys.argv[0]))
#   初始化Bot对象
Bot = Bot.Bot(ip, hp, wp)
print(f'即将启动 {Plugins_name} 服务，目标位于http://%s:%s/ & ws://%s:%s' % (ip, hp, ip, wp))
if Plugins_info != '':
    print(f'{Plugins_info}')
print('高性能しぶそうしん機 !!')

#   初始化一个事件监听器
Listener = Listener.Listener(ip, hp, wp)

#   启动Websocket服务
asyncio.run(Bot.run(receivegroupmsg, receiveprivatemsg))
