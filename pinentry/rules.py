import jam.session

class Pinentry(jam.session.ConfigureSession):

    url = "ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-0.8.1.tar.gz"
    hash = { "md5" : "81f99904daee5331eb6738408bb024b6",
             "sha1" : "84a6940175b552a8562b4014f4661dec3ff10165" }
    version = "0.8.1"
    name = "pinentry"

    configure_args = ["--enable-pinentry-qt4",
                      "--disable-pinentry-gtk2",
                      "--enable-pinentry-curses",
                      "--disable-pinentry-gtk",
                      ]

    depends = ["libiconv", "qt4", "ncurses", "pkg-config"]
