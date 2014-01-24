from kaizen.rules import PythonRules


class PythonDocutils(PythonRules):

    url = "http://pypi.python.org/packages/source/d/docutils/" \
          "%(name)s-%(version)s.tar.gz"
    version = "0.11"
    name = "docutils"
    hash = {
        "md5": "20ac380a18b369824276864d98ec0ad6",
        "sha1": "3894ebcbcbf8aa54ce7c3d2c8f05460544912d67",
    }

    src_path = "%(src_dir)s/%(name)s-%(version)s"
