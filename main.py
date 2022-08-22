import asyncio
import threading
import configparser

import Bot
import setu


def receiveGroupMsg(group_id, user_id, msg):
    if msg == 'setu':
        # Bot.sendGroupMsg(group_id, '[CQ:image,file=' + setu.getSetuUrl() + ",c=8]")
        Bot.sendGroupMsg(group_id, '别着急，涩图马上就来啦。')
        threading.Thread(target=setu.sendSetuG, args=(group_id, Bot.sendGroupMsg)).start()
        #   setu.sendSetuG(group_id, Bot.sendPrivateMsg)
    return


def receivePrivateMsg(user_id, msg):
    #   Bot.sendPrivateMsg(user_id,f'你发送了：{msg}')
    if msg == 'setu':
        # Bot.sendPrivateMsg(user_id, '[CQ:image,file=' + setu.getSetuUrl() + ",c=8]")
        Bot.sendPrivateMsg(user_id, '别着急，涩图马上就来啦。')
        threading.Thread(target=setu.sendSetuP, args=(user_id, Bot.sendPrivateMsg)).start()
    return


config = configparser.ConfigParser()
config.read('./config.ini')
ip = config['Bot']['ip']
hp = config['Bot']['hp']
wp = config['Bot']['wp']
Bot = Bot.Bot(ip, hp, wp)
asyncio.run(Bot.run(receiveGroupMsg, receivePrivateMsg))
