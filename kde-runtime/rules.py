import kaizen.rules

class Kderuntime(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(version)s/src/kde-runtime-%(version)s.tar.bz2"
    hash = { "md5" : "571563f6ab330348d3f917abdf9c69e4",
             "sha1" : "5e1e98535529a67f8d20e8c76d051c81604d7064" }
    version = "4.8.0"
    name = "kde-runtime"

    depends = ["kdelibs", "oxygen-icons"]

    configure_args = ["-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                     ]
