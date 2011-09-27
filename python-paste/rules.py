import jam.session

class Pythonpaste(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/P/Paste/Paste-1.7.5.1.tar.gz"
    hash = { "md5" : "7ea5fabed7dca48eb46dc613c4b6c4ed",
             "sha1" : "11d3c5a2dc52c5e725139a9334574291a0f9d04f" }
    version = "1.7.5.1"
    name = "Paste"

    depends = ["python-distribute"]
