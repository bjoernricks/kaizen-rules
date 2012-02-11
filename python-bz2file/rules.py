import jam.session

class Pythonbz2file(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/b/bz2file/bz2file-%(version)s.tar.gz"
    hash = { "md5" : "e3e7021e373228422d32f15bd01d065e",
             "sha1" : "16f93d17fd03ec8a5bdc84ec028336f2d3b78924" }
    version = "0.9"
    name = "bz2file"
