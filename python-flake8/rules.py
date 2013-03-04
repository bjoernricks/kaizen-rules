import kaizen.rules

class Pythonflake8(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/f/flake8/flake8-%(version)s.tar.gz"
    hash = { "md5" : "176c6b3613777122721db181560aa1e3",
             "sha1" : "dc1b211ba226b3e9872fedc27d0a53c055f44f41" }
    version = "2.0"
    name = "flake8"
    depends = ["python-mccabe", "python-pep8", "python-pyflakes"]
