import kaizen.rules

class Pythondulwich(kaizen.rules.PythonRules):

    url = "http://www.samba.org/~jelmer/dulwich/dulwich-%(version)s.tar.gz"
    hash = { "md5" : "544724f9ac9fe6f9865526917ad284d9",
             "sha1" : "b4e55125fd21908df02fa78efc3868a99636a2cb" }
    version = "0.8.5"
    name = "dulwich"
