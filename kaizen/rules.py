import kaizen.rules

from kaizen.system import Copy, Mkdirs, NoneFile

class Kaizen(kaizen.rules.PythonDevelopRules):

    src_path = "%(package_path)s"
    build_path = "%(package_path)s"
    version = "0.1"
    name = "kaizen"

    # depend on python-bz2file for multiprocess .bz2 archives and
    # depend on python-pyliblzma for lzma compresses .xz archives.
    # depend on python-quilt for patch file handling
    runtime_depends = ["python-bz2file", "python-pyliblzma", "python-quilt"]

    extract = NoneFile

    def post_destroot(self):
        dest_path = self.dest_path + "/bin"
        Mkdirs(dest_path).run()
        Copy(self.package_path + "/bin/kaizen", dest_path).run()
