from flask import *
from setting import SETTING

_KEEP_RUNNING, _WEBHOOK_MODE = True, True

class SERVER():
    app = Flask(__name__)

    def __init__(self):
        setting = SETTING()

        if not _KEEP_RUNNING:
            exit()

        self.app.config['SECRET_KEY'] = setting.FLASK['SECRET_KEY']

