import kaizen.rules

class PerlXmlsax(kaizen.rules.PerlRules):

    url = "http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-SAX-0.99.tar.gz"
    hash = { "md5" : "290f5375ae87fdebfdb5bc3854019f24",
             "sha1" : "9685c417627d75ae18ab0be3b1562608ee093d5c" }
    version = "0.99"
    name = "xml-sax"
    src_path = "%(src_dir)s/XML-SAX-%(version)s"

    depends = ["perl-xml-sax-base"]

    # currently it doesn't install with DESTDIR
    # see https://rt.cpan.org/Public/Bug/Display.html?id=62330
