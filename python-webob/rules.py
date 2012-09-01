import kaizen.rules

class Pythonwebob(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/W/WebOb/WebOb-%(version)s.tar.gz"
    hash = { "md5" : "07d1a1a4b0bf0faa67cb6638c632ea61",
             "sha1" : "32793f14b1d63af3ce3ed965b214e4ce69404863" }
    version = "0.9.8"
    name = "WebOb"

    depends = ["python-distribute"]
