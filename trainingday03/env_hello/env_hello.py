import os


def env_hello():
    k = os.environ['LANG']
    if k[:5] == 'fr_FR':
        return 'Bonjour!'
    return 'Hello!'
