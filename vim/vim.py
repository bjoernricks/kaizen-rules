import jam.session

from jam.system import Copy

class Vim(jam.session.ConfigureSession):

    url = "http://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2"
    hash = { "md5" : "5b9510a17074e2b37d8bb38ae09edbf2",
             "sha1" : "46faa96c5fab639899b1c655c23d8755b62f036f" }
    version = "7.3"
    name = "vim"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    src_path = "%(src_dir)s/vim73"

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additonal parameters to configure script
    args = ["--enable-cscope",
            "--enable-pythoninterp",
            "--enable-multibyte",
            "--disable-netbeans",
            "--disable-gui",
            ]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]

    def configure(self):
        Copy(self.src_path, self.build_path).run()
        super(Vim, self).configure()
