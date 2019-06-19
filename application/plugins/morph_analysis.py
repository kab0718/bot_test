from slackbot.bot import respond_to, listen_to
import MeCab

@listen_to('(.*)')
def hello(message, something):
    m = MeCab.Tagger("-Ochasen")
    message.reply(m.parse(something))