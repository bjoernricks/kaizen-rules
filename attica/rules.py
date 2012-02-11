import jam.session

class Attica(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/attica/attica-%(version)s.tar.bz2"
    hash = { "md5" : "5a77f678422e7a52e3a3abb2d7ad0499",
             "sha1" : "ed1d6f49bbc2362464346c4066eb4eaade69a08b" }
    version = "0.3.0"
    name = "attica"

    depends = ["qt4"]
