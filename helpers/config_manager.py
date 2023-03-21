import configparser


class ConfigManager():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')


    def get_discord_token(self):
        return self.config.get('TOKENS', 'DISCORD_TOKEN')
    
    
    def get_temp_text_category_id(self):
        return int(self.config.get('CATEGORIES', 'TEMPORARY_TEXT'))
    

    def get_temp_voice_category_id(self):
        return int(self.config.get('CATEGORIES', 'TEMPORARY_VOICE'))
    

    def get_maximum_temp_text_channels(self):
        return int(self.config.get('CHANNELS', 'MAXIMUM_TEMP_TEXT'))
    

    def get_maximum_temp_voice_channels(self):
        return int(self.config.get('CHANNELS', 'MAXIMUM_TEMP_VOICE'))
    
