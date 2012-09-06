import kaizen.rules

class Patch(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnu.org/gnu/patch/patch-%(version)s.tar.bz2"
    hash = { "md5" : "0818d1763ae0c4281bcdc63cdac0b2c0",
             "sha1" : "105f313d14b5458e0aa229c518bda9ebdf921a1b" }
    version = "2.6.1"
    name = "patch"
