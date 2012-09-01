from kaizen.rules import PythonRules

class PythonDocutils(PythonRules):

    url = "http://prdownloads.sourceforge.net/docutils/docutils-0.7.tar.gz?download"
    version = "0.7"
    name = "docutils"

    src_path = "%(src_dir)s/%(name)s-%(version)s"
