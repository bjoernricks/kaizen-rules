import kaizen.rules

class Oxygengtk(kaizen.rules.CMakeRules):

    url = "http://ftp.gwdg.de/pub/x11/kde/stable/oxygen-gtk/1.1.3/src/oxygen-gtk-%(version)s.tar.bz2"
    hash = { "md5" : "e3b280a61cbe4363c41c26083e94643d",
             "sha1" : "d1b1029e1e2e5d073d8e87a53c4814ab3eae4820" }
    version = "1.1.3"
    name = "oxygen-gtk"
