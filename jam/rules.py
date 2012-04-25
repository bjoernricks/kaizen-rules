import jam.session

from jam.system import Copy, Mkdirs, NoneFile

class Jam(jam.session.PythonDevelopSession):

    src_path = "%(package_path)s"
    build_path = "%(package_path)s"
    version = "0.1"
    name = "jam"

    # depend on python-bz2file for multiprocess .bz2 archives and
    # depend on python-pyliblzma for lzma compresses .xz archives.
    runtime_depends = ["python-bz2file", "python-pyliblzma"]

    extract = NoneFile

    def post_destroot(self):
        dest_path = self.dest_path + "/bin"
        Mkdirs(dest_path).run()
        Copy(self.package_path + "/bin/jam", dest_path).run()
