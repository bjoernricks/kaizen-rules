import kaizen.rules

class Django(kaizen.rules.PythonRules):

    url = ["https://www.djangoproject.com/download/%(version)s/tarball/",
           "django-%(version)s.tar.gz"]
    hash = { "md5" : "6ffecdc01ad360e1abdca1015ae0893a",
             "sha1" : "ccee9f589b819545f9d71d4aee2c2322e5cc2fd6" }
    version = "1.4.2"
    name = "Django"
