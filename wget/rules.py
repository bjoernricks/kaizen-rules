import kaizen.rules

class Wget(kaizen.rules.ConfigureRules):

    url = "http://ftp.gnu.org/gnu/wget/wget-1.12.tar.bz2"
    hash = { "md5" : "308a5476fc096a8a525d07279a6f6aa3" }
    version = "1.12"
    name = "wget"

