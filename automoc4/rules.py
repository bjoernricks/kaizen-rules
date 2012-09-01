import kaizen.rules

class Automoc4(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(name)s/%(version)s/%(name)s-%(version)s.tar.bz2"
    hash = { "md5" : "91bf517cb940109180ecd07bc90c69ec",
             "sha1" : "d864c3dda99d8b5f625b9267acfa1d88ff617e3a" }
    version = "0.9.88"
    name = "automoc4"
