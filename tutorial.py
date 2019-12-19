from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')




client = TutorialPlugin()
client.run('5SpcgbVpQEbc3s8iLEyr9jh8D7uSy2Sb')
