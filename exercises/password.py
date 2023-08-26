import hashlib
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits as ascii_digits,
    punctuation
)
import random


def generate_password(len, uppercase=False, digits=False, symbols=False):
    gen_pool = ascii_lowercase
    if uppercase:
        gen_pool += ascii_uppercase
    if digits:
        gen_pool += ascii_digits
    if symbols:
        gen_pool += punctuation
    return ''.join(random.choice(gen_pool) for _ in range(len))


class PasswordGeneratorAdapter:
    def generate_password(self, length, options):
        default_options = {
            'uppercase': False,
            'digits': False,
            'symbols': False,
        }
        prepared_options = {key: True for key in options}
        final_options = {**default_options, **prepared_options}
        return generate_password(length, **final_options)


class PasswordBuilder:
    def __init__(self, passwordGenerator):
        self.passwordGenerator = passwordGenerator

    def build_password(self, len=10, options=[]):
        password = self.passwordGenerator.generate_password(len, options)
        m = hashlib.sha1()
        m.update(password.encode())
        digest = m.hexdigest()

        return {'password': password, 'digest': digest}
    
builder = PasswordBuilder(PasswordGeneratorAdapter())
a = builder.build_password()
print(a)
