import kaizen.rules

class Libiodbc(kaizen.rules.ConfigureRules):

    url = "http://www.iodbc.org/downloads/iODBC/libiodbc-%(version)s.tar.gz"
    hash = { "md5" : "ddbd274cb31d65be6a78da58fc09079a",
             "sha1" : "53988878b6897d5ce7b8f62138f1f7e0e40b7d4f" }
    version = "3.52.7"
    name = "libiodbc"

    configure_args = ["--disable-gui", "--disable-gtktest",
                      "--with-iodbc-inidir=%(prefix)s/etc"]
