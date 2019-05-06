import time

from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()


def color_print(msg):
    print('\033[1;31;43m%s\033[0m' % msg)


@bot.register()
def print_others(msg):
    sender = msg.sender.name
    color_print('sender is %s ' % sender)
    bot.file_helper.send(msg)
    print(msg)


# 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)


# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')


# friends = bot.friends()
# receiver = bot.friends().search('伍云聪')[0]
# for i in range(100):
#     time.sleep(1)
#     receiver.send("我的装备全部清零了怎么回事啊")

embed()
