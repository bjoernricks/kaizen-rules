import jam.session

class Libdaemon(jam.session.ConfigureSession):

    url = "http://0pointer.de/lennart/projects/libdaemon/libdaemon-%(version)s.tar.gz"
    hash = { "md5" : "509dc27107c21bcd9fbf2f95f5669563",
             "sha1" : "78a4db58cf3a7a8906c35592434e37680ca83b8f" }
    version = "0.14"
    name = "libdaemon"

    depends = ["pkg-config"]

    configure_args = ["--disable-lynx"]
