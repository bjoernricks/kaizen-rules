import jam.session

class Kdelibs(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(version)s/src/kdelibs-%(version)s.tar.bz2"
    hash = { "md5" : "c19858c68f9a209ae521d7fb3c34747b",
             "sha1" : "5e4744405734e6c3ce572ef7d16054390692b38a" }
    version = "4.8.0"
    name = "kdelibs"

    depends = ["qt4", "perl", "zlib", "strigi", "attica", "openssl",
               "soprano", "shared-desktop-ontologies", "dbus", "libdbusmenu-qt",
               "automoc4", "xz", "bzip2", "pcre", "libjpeg", "avahi",
               "giflib", "docbook-xsl", "docbook-xml", "grantlee", "qca"]

    configure_args = ["-DWITH_ENCHANT=ON",
                      "-DWITH_Soprano=ON",
                      "-DKDE_DEFAULT_HOME=Library/Preferences/KDE",
                      "-DWITH_HSPELL=OFF",
                      "-DWITH_FAM=OFF",
                      "-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                      # "-DKDE_DISTRIBUTION_TEXT=jam software manager",
                      "-DCMAKE_BUILD_TYPE=Release",
                      ]
