import kaizen.rules

class Giflib(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/giflib/giflib%%204.x/giflib-%(version)s/giflib-%(version)s.tar.bz2"
    hash = { "md5" : "7125644155ae6ad33dbc9fc15a14735f",
             "sha1" : "22680f604ec92065f04caf00b1c180ba74fb8562" }
    version = "4.1.6"
    name = "giflib"

