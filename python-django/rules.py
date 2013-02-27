import kaizen.rules

class Django(kaizen.rules.PythonRules):

    url = ["https://www.djangoproject.com/download/%(version)s/tarball/",
           "django-%(version)s.tar.gz"]
    hash = { "md5" : "851d00905eb70e4aa6384b3b8b111fb7",
             "sha1" : "1bfaa4643c6775fbf394137f1533659be45441e7" }
    version = "1.4.5"
    name = "Django"
