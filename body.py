from flask import *
from _setting import SETTING
from _html import HTML

_KEEP_RUNNING, _WEBHOOK_MODE = True, True

app = Flask(__name__)
setting = SETTING()
html = HTML()

if not _KEEP_RUNNING:
    exit()

app.config['SECRET_KEY'] = setting.FLASK['SECRET_KEY']


@app.route("/css/<path:filename>")
def _CSS(filename):
    return send_from_directory("./html/css/", filename=filename)


@app.route("/js/<path:filename>")
def _JS(filename):
    return send_from_directory("./html/js/", filename=filename)


@app.route("/")
def _ROOT():
    return html.index

app.run(host="0.0.0.0", port=setting.FLASK['PORT'])