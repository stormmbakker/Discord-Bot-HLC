from config import Settings


def print_hi(name):
    config = Settings()
    print(config.discord_token)


if __name__ == '__main__':
    print_hi('PyCharm')
