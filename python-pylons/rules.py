import kaizen.rules

class Pythonpylons(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/P/Pylons/Pylons-%(version)s.tar.gz"
    hash = { "md5" : "93ae0bf3d33fffc35f8ab16a749b3630",
             "sha1" : "5c30594aae78fe0cce5132a94412923becd7f377" }
    version = "0.10"
    name = "Pylons"

    depends = ["python-babel", "python-routes", "python-webhelpers",
               "python-beaker", "python-paste", "python-pastedeploy",
               "python-pastescript", "python-formencode", "python-simplejson",
               "python-decorator", "python-nose", "python-mako",
               "python-webob", "python-weberror", "python-webtest",
               "python-tempita", "python-pygments"]
