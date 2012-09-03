import kaizen.rules

class Pythonjinja2(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/J/Jinja2/Jinja2-%(version)s.tar.gz"
    hash = { "md5" : "1c49a8825c993bfdcf55bb36897d28a2",
             "sha1" : "f122aeb324b2009bbcee341d0f001a047ac4bbe5" }
    version = "2.6"
    name = "Jinja2"
