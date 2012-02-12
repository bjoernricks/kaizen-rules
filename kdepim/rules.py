import jam.session

class Kdepim(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/4.8.0/src/kdepim-4.8.0.tar.bz2"
    hash = { "md5" : "502216fe546ee87b7bb66f2da5599417",
             "sha1" : "61509f42a96193ae2a9b9f8560dccb73d739f356" }
    version = "4.8.0"
    name = "kdepim"

    depends = ["kdepimlibs", "akonadi", "kdepim-runtime", "qt4", "kdelibs",
               "automoc4", "boost", "zlib", "strigi", "soprano",
               "shared-desktop-ontologies", "grantlee", "libxslt", "boost",
               "libassuan", "cyrus-sasl"]

    configure_args = ["-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",]
