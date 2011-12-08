import jam.session

class Libffi(jam.session.ConfigureSession):

    url = "ftp://sourceware.org/pub/libffi/libffi-3.0.10.tar.gz"
    hash = { "md5" : "79390673f5d07a8fb342bc09b5055b6f",
             "sha1" : "97abf70e6a6d315d9259d58ac463663051d471e1" }
    version = "3.0.10"
    name = "libffi"

    patches = ["patch-configure-darwin11.diff",
               "patch-configure.diff"]
