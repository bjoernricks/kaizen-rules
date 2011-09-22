import jam.session

class Cscope(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/cscope/cscope/15.7a/cscope-15.7a.tar.bz2"
    hash = { "md5" : "da43987622ace8c36bbf14c15a350ec1",
             "sha1" : "f6348694e5443769add851f97fd39365e93dc474" }
    version = "15.7a"
    name = "cscope"

    patches = ["01-ncurses.diff"]
