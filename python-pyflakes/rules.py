import kaizen.rules

class Pythonpyflakes(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/p/pyflakes/pyflakes-%(version)s.tar.gz"
    hash = { "md5" : "00debd2280b962e915dfee552a675915",
             "sha1" : "c868b5d58c7a833e7759e173875b37760691b72a" }
    version = "0.6.1"
    name = "pyflakes"
