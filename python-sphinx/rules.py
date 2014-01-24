import kaizen.rules


class Pythonsphinx(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/S/Sphinx/" \
          "Sphinx-%(version)s.tar.gz"
    hash = {"md5": "104494f036889122c9f403ae065ae7a9",
            "sha1": "448cdb89d96c85993e01fe793ce7786494cbcda7"}
    version = "1.2.1"
    name = "Sphinx"

    depends = ["python-docutils", "python-jinja2", "python-pygments"]
