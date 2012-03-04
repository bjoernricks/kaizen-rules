import jam.session

class Skrooge(jam.session.CMakeSession):

    url = "http://skrooge.org/files/skrooge-1.2.0.tar.bz2"
    hash = { "md5" : "d137d2940f2f7d3dca5432aa652359e9",
             "sha1" : "1587d493f6064637805e3601bdae08fd5258a633" }
    version = "1.2.0"
    name = "skrooge"

    depends = ["kdelibs", "qt4", "automoc4", "perl", "qca"]
