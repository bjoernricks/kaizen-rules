import kaizen.rules

class Oxygenicons(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(version)s/src/oxygen-icons-%(version)s.tar.bz2"
    hash = { "md5" : "2ae26ba235f207eb29677637c1d059a7",
             "sha1" : "cd893bb4060957e4ceff39c46e01cec82746163e" }
    version = "4.8.0"
    name = "oxygen-icons"
