import jam.session

class Kdepimruntime(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(version)s/src/kdepim-runtime-%(version)s.tar.bz2"
    hash = { "md5" : "8f941417152fd2ae9e5130cf0426a95e",
             "sha1" : "1cf75a92ddd0c18891163cd9d7f2290afae17472" }
    version = "4.8.0"
    name = "kdepim-runtime"

    depends = ["akonadi", "shared-mime-info", "kdelibs", "kdepimlibs",
               "libxml2", "soprano", "shared-desktop-ontologies", "strigi",
               "libxslt", "perl", "automoc4", "qt4", "boost",
               ]

    configure_args = [
                      "-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                      "-DKDE_DISTRIBUTION_TEXT=\"jam software manager\"",
                      ]
