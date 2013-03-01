import kaizen.rules

class Django(kaizen.rules.PythonRules):

    url = ["https://www.djangoproject.com/download/%(version)s/tarball/",
           "django-%(version)s.tar.gz"]
    hash = { "md5" : "fac09e1e0f11bb83bb187d652a9be967",
             "sha1" : "358dce7db72904c334e3d7ce7eaa0e27a22cfa16" }
    version = "1.5"
    name = "Django"
