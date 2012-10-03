import kaizen.rules

from kaizen.system import Quilt
from kaizen.rules.groups import KDE

class Kdelibs(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(version)s/src/kdelibs-%(version)s.tar.xz"
    hash = { "md5" : "421a0cb4e51db7d8eb6bb8aff508aeab",
             "sha1" : "e86ee16ac7c412b0f6abe3754cb372a45d41c71b" }
    version = "4.9.2"
    name = "kdelibs"

    groups = [KDE]

    patch_cmd = Quilt

    depends = ["qt4", "perl", "zlib", "strigi", "attica", "openssl",
               "soprano", "shared-desktop-ontologies", "dbus", "libdbusmenu-qt",
               "automoc4", "xz", "bzip2", "pcre", "libjpeg", "avahi",
               "giflib", "docbook-xsl", "docbook-xml", "grantlee", "qca",
               "phonon", "shared-mime-info"]

    configure_cc = "gcc"
    configure_cxx = "g++"
    configure_args = ["-DWITH_ENCHANT=ON",
                      "-DWITH_Soprano=ON",
                      "-DKDE_DEFAULT_HOME=Library/Preferences/KDE",
                      "-DWITH_HSPELL=OFF",
                      "-DWITH_FAM=OFF",
                      "-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                      "-DSHAREDDESKTOPONTOLOGIES_ROOT_DIR=%(prefix)s/share/ontology",
                      # "-DKDE_DISTRIBUTION_TEXT=kaizen software manager",
                      "-DCMAKE_BUILD_TYPE=Release",
                      ]
