import jam.session

class Pythonpygments(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/P/Pygments/%(name)s-%(version)s.tar.gz"
    hash = { "md5" : "ef997066cc9ee7a47d01fb4f3da0b5ff",
             "sha1" : "4fbd937fd5cebc79fa4b26d4cce0868c4eec5ec5" }
    version = "1.5"
    name = "Pygments"
