import json

# Реализуйте класс DatabaseConfigLoader, который отвечает за загрузку конфигурации для базы данных.
class DatabaseConfigLoader():

    def __init__(self, path):
        self.path_to_config = path

    def load(self, env):
        filename = f'database.{env}.json'
        filepath = self.path_to_config / filename
        raw_config = json.loads(open(filepath).read())

        if 'extend' not in raw_config:
            return raw_config

        extend = raw_config['extend']
        rest = {k: v for k, v in raw_config.items() if k != 'extend'}
        return {**self.load(extend), **rest}
