import jam.session

class Intltool(jam.session.ConfigureSession):

    url = "http://launchpad.net/intltool/trunk/0.50.1/+download/intltool-%(version)s.tar.gz"
    hash = { "md5" : "892f9a3e809b55b7c6c8ceae4f1188d6",
             "sha1" : "3964df4057a16c82f711e778df058e6c11fe093a" }
    version = "0.50.1"
    name = "intltool"
