import kaizen.rules

class Akonadi(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/akonadi/src/akonadi-%(version)s.tar.bz2"
    hash = { "md5" : "07e2aa2e6953ac518f9306911747e264",
             "sha1" : "f02302686f6e50be240d1e73280c00a10c8ccf11" }
    version = "1.6.2"
    name = "akonadi"

    configure_args = ["-DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE",
                      "-DAKONADI_BUILD_QSQLITE=TRUE",
                      "-DDATABASE_BACKEND=SQLITE",
                      "-DAKONADI_BUILD_TESTS=FALSE",
                      "-DCMAKE_BUILD_TYPE=Release",
                      "-DAKONADI_BUNDLE_PATH=%(apps_dir)s/KDE4",
                     ]

    depends = ["qt4", "automoc4", "shared-mime-info", "boost", "soprano",
               "dbus", "sqlite3"]
