import kaizen.rules

class Phonon(kaizen.rules.CMakeRules):

    url = "phonon-4.6.0.tar.bz2"
    hash = { "md5" : "7b194cc3a5583c958f81bb41e0f044cb",
             "sha1" : "dd7aabe789144d2263b596873eb34b57cc3a16a2" }
    version = "4.6.0"
    name = "phonon"

    depends = ["qt4",
               "automoc4",
               ]
