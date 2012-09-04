import kaizen.rules

class Oxygengtk2(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk2/1.3.0/src/oxygen-gtk2-1.3.0.tar.bz2"
    hash = { "md5" : "9c9d996904db3f4897772788f3bf1599",
             "sha1" : "5c0952c493bc8aab996f886f141f108bb21e75bc" }
    version = "1.3.0"
    name = "oxygen-gtk2"

    depends = ["pkg-config", "gtk2", "cairo"]
