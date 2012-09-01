import kaizen.rules

class Amarok(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/amarok/2.5.0/src/amarok-2.5.0.tar.bz2"
    hash = { "md5" : "b7983eaa33e4771769ae9e330c811995",
             "sha1" : "9849900d20225e703c43d242650a8fa211cf15f2" }
    version = "2.5.0"
    name = "amarok"

    # configure_args = [""]

    depends = ["taglib",
               "kdelibs",
               "kde-runtime",
               "qtscriptgenerator",
               "qca",
               "libmtp",
               "libgpod",
               "mysql",
               "phonon",
               "zlib",
               "taglib-extras",
               ]
