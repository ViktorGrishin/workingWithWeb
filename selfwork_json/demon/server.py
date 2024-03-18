import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            'fireplace': [69, 239, 256, 124, 58, 147, 77],
            'room': [171, 298, 262, 124, 279, 153],
            'meadow': [89, 129, 112, 162, 299, 170],
            'courtyard': [7, 53, 47, 198]
        },
        {
            'mountain': [178, 124, 282, 156, 183, 265, 3],
            'courtyard': [37, 232, 102],
            'lake': [130, 118, 224]
        }
    ]

    index = 0
    index = int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))
    while index not in (1, 2):
        index = int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))
        ...
    server = Server('127.0.0.1', 5000, data[index - 1])
    with server.run():
        row =  input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')
        while row != 'stop':
            ...