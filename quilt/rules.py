from kaizen.rules import ConfigureRules
from kaizen.system import Make

class Quilt(ConfigureRules):

    url = "http://download.savannah.gnu.org/releases/quilt/quilt-%(version)s.tar.gz"
    hash = { "md5" : "058a08a9b626bdec9ec8c519dc92158c",
             "sha1" : "c93c79598c55ba288f60babcc74a9fc9b04404b6" }
    version = "0.60"
    name = "quilt"

    depends = ["gnu-sed"]

    build_path = "%(src_path)s"

    configure_args = ["--with-sed=%(prefix)s/bin/gsed",
                      "--without-getopt",
                      "--without-rpmbuild"]

    def destroot(self):
        Make(self.build_path, self.config.get("debug")).run(["BUILD_ROOT="
             + self.dest_dir, "install"])

