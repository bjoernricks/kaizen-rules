import kaizen.rules

class Perlxmlsaxbase(kaizen.rules.PerlRules):

    url = "http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-SAX-Base-%(version)s.tar.gz"
    hash = { "md5" : "38c8c3247dfd080712596118d70dbe32",
             "sha1" : "5ae6a06e465daa65e1a69d1a6977299084fe9aef" }
    version = "1.08"
    name = "xml-sax-base"
    parallel = False

    src_path = "%(src_dir)s/XML-SAX-Base-%(version)s"
