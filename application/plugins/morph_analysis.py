from slackbot.bot import respond_to, listen_to

@listen_to('私は(.*)です')
def hello(message, something):
    message.reply('こんにちは！{0}さん！'.format(something))