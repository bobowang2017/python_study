from robot.app import bot

receiver = bot.friends().search('潘思童')[0]
receiver.send("bobo")
