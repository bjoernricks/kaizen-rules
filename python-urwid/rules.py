import kaizen.rules

class Pythonurwid(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/u/urwid/urwid-%(version)s.tar.gz"
    hash = { "md5" : "932d199de6fc847eab2c151512220665",
             "sha1" : "0d6aa34975bb516565cfbf951487d26161e400b7" }
    version = "1.1.1"
    name = "urwid"
