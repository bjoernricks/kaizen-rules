import kaizen.rules

class Pythonsphinx(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/S/Sphinx/Sphinx-%(version)s.tar.gz"
    hash = { "md5" : "b65a5d5d6172f3dcfefb4770ec63926e",
             "sha1" : "92f422474e43345ab69dedceeedfd7d18c55da2d" }
    version = "1.1.2"
    name = "Sphinx"

    depends = ["python-jinja2"]
