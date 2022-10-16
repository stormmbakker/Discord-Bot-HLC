import yaml


class Settings:
    def __init__(self):
        with open("settings.yaml", "r") as f:
            settings = yaml.load(f, Loader=yaml.FullLoader)
            self.discord_token = settings['app settings']['discord']['token']
