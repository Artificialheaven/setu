import asyncio
import threading
import configparser

import Bot
import setu


def receiveGroupMsg(group_id, user_id, msg):
    if msg == 'setu':
        Bot.sendGroupMsg(group_id, '别着急，涩图马上就来啦。')
        threading.Thread(target=setu.sendSetuG, args=(group_id, Bot.sendGroupMsg)).start()
    return


def receivePrivateMsg(user_id, msg):
    if msg == 'setu':
        Bot.sendPrivateMsg(user_id, '别着急，涩图马上就来啦。')
        threading.Thread(target=setu.sendSetuP, args=(user_id, Bot.sendPrivateMsg)).start()
    return


config = configparser.ConfigParser()
config.read('./config.ini')
ip = config['Bot']['ip']
hp = config['Bot']['hp']
wp = config['Bot']['wp']
Bot = Bot.Bot(ip, hp, wp)
print('即将启动 setu 服务，目标位于http://%s:%s/ & ws://%s:%s' % (ip, hp, ip, wp))
print('高性能しぶそうしん機 !!')

asyncio.run(Bot.run(receiveGroupMsg, receivePrivateMsg))