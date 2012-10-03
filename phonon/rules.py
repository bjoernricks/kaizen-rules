import kaizen.rules

class Phonon(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/phonon/%(version)s/src/phonon-%(version)s.tar.xz"
    hash = { "md5" : "bbe0c1c62ed14c31479c4c1a6cf1e173",
             "sha1" : "d8dbc188b58c6dd9c6a73d3742a25291e647bb95" }
    version = "4.6.0"
    name = "phonon"

    depends = ["qt4",
               "automoc4",
               "glib2"]
