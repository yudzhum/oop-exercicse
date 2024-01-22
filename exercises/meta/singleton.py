def singleton(cls):
    class NewClass:
        isinstances = []

        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)

    return NewClass


@singleton
class Logger:
    pass


@singleton
class AppConfig:
    pass


@singleton
class SMTPServerConfig:
    pass


log = Logger()
print(log)
app_conf = AppConfig()
app_conf_2 = AppConfig()
smtp_conf = SMTPServerConfig()
assert log is Logger()
assert app_conf is app_conf_2
assert smtp_conf is SMTPServerConfig()
assert log is not app_conf
assert log is not smtp_conf
assert app_conf is not smtp_conf
print('Good')