import os.path
import jam.session

from jam.system import Copy, Configure

class Git(jam.session.ConfigureSession):

    url =  "http://git-core.googlecode.com/files/git-%(version)s.tar.gz"
    hash = { "md5" : "ab2716db51580037c7ebda4c8e9d56eb",
             "sha1" : "501ee8685c148d377950e42c111e01d83fd1d41a" }
    version = "1.7.10"
    name = "git"

    depends = ["python", "gettext", "git-manpages", "perl", "openssl",
               "libcurl", "zlib", "libexpat"]

    configure_args = [
                      "--with-gitconfig=etc/gitconfig",
                      "--with-gitattributes=etc/gitattributes",
                     ]

    def pre_configure(self):
        Copy(self.src_path + "/*", self.build_path).run()

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "contrib", "completion",
                          "git-completion.bash"),
             os.path.join(self.dest_path, "etc",
                          "bash_completion.d", "git")).run()
        Copy(os.path.join(self.session_path, "contrib", "giteditor"),
             os.path.join(self.dest_path, "share", "git",
                          "contrib", "giteditor")).run()

    def distclean(self):
        Delete(self.build_path).run()
