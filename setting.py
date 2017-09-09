import json, codecs


class SETTING():
    def __init__(self):
        global _KEEP_RUNNING, _WEBHOOK_MODE
        settingJson = json.loads(codecs.open("./settings.json","r",encoding='UTF-8').read())

        if "FLASK" in settingJson.keys():
            self.FLASK = settingJson['FLASK']
        else:
            print("\t\t-*-*- FLASK Setting Not Found -*-*-")
            _KEEP_RUNNING = False
            exit()

        if "DB" in settingJson.keys():
            self.DB = settingJson['DB']
        else:
            print("\t\t-*-*- DB Setting Not Found -*-*-")
            _KEEP_RUNNING = False
            exit()

        if "WEBHOOK" in settingJson.keys():
            self.WEBHOOK = settingJson['WEBHOOK']
        else:
            print("\t\t-*-*- WebHook Mode Disabled -*-*-")
            _WEBHOOK_MODE = False

    def extractDBInfo(self):
        return self.DB
