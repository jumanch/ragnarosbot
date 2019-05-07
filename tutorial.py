from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')




client = TutorialPlugin()
client.run('Bm7ITbmb1Y6q6Kp7mt6OF-xI_kj_LwXY')