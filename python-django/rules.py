import os.path
import kaizen.rules

from kaizen.system import Copy

class Django(kaizen.rules.PythonRules):

    url = ["https://www.djangoproject.com/download/%(version)s/tarball/",
           "django-%(version)s.tar.gz"]
    hash = { "md5" : "fac09e1e0f11bb83bb187d652a9be967",
             "sha1" : "358dce7db72904c334e3d7ce7eaa0e27a22cfa16" }
    version = "1.4.5"
    name = "Django"

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "extras", "django_bash_completion"),
             os.path.join(self.dest_path, "etc",
                          "bash_completion.d", "django_bash_completion")).run()
