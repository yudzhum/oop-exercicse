# Singleton
class Logger:
    __instance = None
    log_level = 'INFO'

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def get_logger():
        if not Logger.__instance:
            Logger.__new__(Logger)
        return Logger.__instance
    
    @classmethod
    def set_level(cls, value):
        if not cls.__instance:
            raise ValueError('The instance has not created')
        cls.log_level = value
