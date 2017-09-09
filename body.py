from flask import *
from _setting import SETTING
from _html import HTML

_KEEP_RUNNING, _WEBHOOK_MODE = True, True

class _SERVER():
    app = Flask(__name__)

    def __init__(self):
        self.setting = SETTING()
        self.html = HTML()

        if not _KEEP_RUNNING:
            exit()

        self.app.config['SECRET_KEY'] = self.setting.FLASK['SECRET_KEY']

    def run(self, host="0.0.0.0", port=80):
        self.app.run(host=host, port=port)

project = _SERVER()
project.run()