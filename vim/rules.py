import jam.session

from jam.system import Copy

class Vim(jam.session.ConfigureSession):

    url = "http://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2"
    hash = { "md5" : "5b9510a17074e2b37d8bb38ae09edbf2",
             "sha1" : "46faa96c5fab639899b1c655c23d8755b62f036f" }
    version = "7.3"
    name = "vim"

    src_path = "%(src_dir)s/vim73"

    configure_args = ["--enable-cscope",
                      "--enable-pythoninterp=yes",
                      "--enable-multibyte",
                      "--disable-netbeans",
                      "--disable-gui",
                      "--with-local-dir=%(prefix)s",
                     ]

    depends = ["ctags", "cscope", "gettext", "libiconv"]

    def pre_configure(self):
        Copy(self.src_path, self.build_path).run()
