

class Config:
    __instance: 'Config' = None

    def __init__(self):
        if Config.__instance is not None:
            raise Exception()
        else:
            Config.__instance = self

    @staticmethod
    def get():
        if Config.__instance is None:
            Config()

        return Config.__instance
