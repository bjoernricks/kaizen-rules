import os.path
import jam.session

from jam.system import Copy, Configure

class Git(jam.session.ConfigureSession):

    url =  "http://git-core.googlecode.com/files/git-%(version)s.tar.gz"
    hash = { "md5" : "9abd782299d897b416811c81ad78740b",
             "sha1" : "71c5a5acdef77cd8d29a4ae5d4fe7f2889f495b5" }
    version = "1.7.9.6"
    name = "git"

    depends = ["python", "gettext", "git-manpages"]

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
