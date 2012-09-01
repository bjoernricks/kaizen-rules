import kaizen.rules

class Cyrussasl(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-2.1.25.tar.gz"
    hash = { "md5" : "341cffe829a4d71f2a6503d669d5a946",
             "sha1" : "b6c34426012d9b5d448d5646cbecd818a5eeacbf" }
    version = "2.1.25"
    name = "cyrus-sasl"

    depends = ["openssl"]

    parallel = False

    patches = ["patch-config_ltconfig.diff"]

    configure_args = ["--with-dbpath=%(prefix)s/etc/sasldb2",
                      "--with-plugindir=%(prefix)s/lib/sasl2",
                      "--with-saslauthd=%(prefix)s/var/state/saslauthd",
                      "--with-pwcheck=%(prefix)s/var/pwcheck",
                      "--disable-macos-framework",
                      "--enable-srp",
                      "--enable-srp-setpass",
                      "--enable-login",
                      "--enable-ntlm",
                      "--with-rc4=openssl"]
