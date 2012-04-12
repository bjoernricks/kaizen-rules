import jam.session

class Calligra(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/calligra-latest/calligra-%(version)s.tar.bz2"
    hash = { "md5" : "a45b9141c6bb750569e8f6554197dd50",
             "sha1" : "6026f4ddcf4bf647ea13dfb477233df472a5c007" }
    version = "2.4.0"
    name = "calligra"

    depends = ["kdelibs", "qt4", "attica", "perl", "zlib", "libpng", "boost",
               "kdepimlibs", "qca", "soprano", "eigen", "freetype", "fontconfig"]

    configure_args = ["-DIHAVEPATCHEDQT=TRUE"]
