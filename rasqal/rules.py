import kaizen.rules

class Rasqal(kaizen.rules.ConfigureRules):

    url = "http://download.librdf.org/source/rasqal-%(version)s.tar.gz"
    hash = { "md5" : "a3662b8d9efef9d8ef0a3c182450fba2",
             "sha1" : "9a685d7aa0a1de59e7547c1426fd8b4713fdbd9a" }
    version = "0.9.28"
    name = "rasqal"

    depends = ["libxml2", "pkg-config", "libxslt", "raptor2"]
