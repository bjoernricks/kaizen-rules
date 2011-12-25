import os.path
import jam.session

from jam.system import Command, Copy

class Boost(jam.session.Session):

    url = "http://downloads.sourceforge.net/project/boost/boost/1.48.0/boost_1_48_0.tar.bz2"
    hash = { "md5" : "d1e9a7a7f532bb031a3c175d86688d95",
             "sha1" : "27aced5086e96c6f7b2b684bda2bd515e115da35" }
    version = "1.48.0"
    name = "boost"

    src_path = "%(src_dir)s/boost_1_48_0/"

    configure_args = ["--prefix=%(prefix)s", 
                      "--without-libraries=mpi",
                      ]

    build_args = ["--build-dir=%(build_path)s"]

    depends = ["python", "zlib", "expat", "libiconv"]

    def configure(self):
        cmd = os.path.join(self.src_path, "bootstrap.sh")
        Command(cmd, self.configure_args, self.src_path, self.debug).run()

    def build(self):
        cmd = os.path.join(self.src_path, "b2")
        Command(cmd, self.build_args, self.src_path, self.debug).run()

    def destroot(self):
        cmd = os.path.join(self.src_path, "bjam")
        args = ["install", "--prefix=" + self.dest_path]
        Command(cmd, args, self.src_path, self.debug).run()

    def clean(self):
        cmd = os.path.join(self.src_path, "bjam")
        args = ["--clean"]
        Command(cmd, args, self.src_path, self.debug).run()
