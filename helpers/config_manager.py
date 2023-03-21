import configparser


class ConfigManager():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


    def get_discord_token(self):
        return self.config.get('TOKENS', 'DISCORD_TOKEN')