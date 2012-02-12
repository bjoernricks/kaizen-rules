import jam.session

from jam.system import Copy, Mkdirs

class Jam(jam.session.PythonDevelopSession):

    src_path = "%(package_path)s"
    build_path = "%(package_path)s"
    version = "0.1"
    name = "jam"

    runtime_depends = ["python-bz2file"]

    def post_destroot(self):
        dest_path = self.dest_path + "/bin"
        Mkdirs(dest_path).run()
        Copy(self.package_path + "/bin/jam", dest_path).run()
