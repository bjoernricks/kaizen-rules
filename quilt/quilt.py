from jam.session import ConfigureSession
from jam.system import Make

class Quilt(ConfigureSession):

    url = "http://download.savannah.gnu.org/releases/quilt/quilt-0.48.tar.gz"
    hash = { "md5" : "f77adda60039ffa753f3c584a286f12b" }
    version = "0.48"
    name = "quilt"

    depends = ["gnu-sed"]
    
    build_path = "%(src_path)s"
    
    args = ["--with-sed=%(prefix)s/bin/gsed",
            "--without-getopt",
            "--without-rpmbuild"]

    def destroot(self):
        Make(self.build_path, self.config.get("debug")).run(["BUILD_ROOT=" 
             + self.dest_dir, "install"])

