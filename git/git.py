import os.path
import jam.session

from jam.system import Copy, Configure

class Git(jam.session.ConfigureSession):

    url = "http://www.kernel.org/pub/software/scm/git/git-1.7.6.tar.bz2"
    hash = { "md5" : "9e0a438eb71e89eedb61f89470ed32a0",
             "sha1" : "c519b0765c419c84b561bb4a2a86526b16d95cde" }
    version = "1.7.6"
    name = "git"

    args = [
            "--with-gitconfig=etc/gitconfig",
            "--with-gitattributes=etc/gitattributes",
            ]

    def configure(self):
        Copy(self.src_path, self.build_path).run()
        args = self.args
        args.append("--prefix=" + self.prefix)
        Configure(args, self.build_path, self.build_path,
                  self.debug).run()

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "contrib", "completion",
                          "git-completion.bash"),
             os.path.join(self.destroot_path + self.prefix, "etc",
                          "bash_completion.d", "git")).run()
