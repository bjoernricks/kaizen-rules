import kaizen.rules

class Kdepimlibs(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/4.8.0/src/kdepimlibs-4.8.0.tar.bz2"
    hash = { "md5" : "3e1ea1d5f56eb87c0c305d941ac414c0",
             "sha1" : "22409015a8047e3a78711093e3363775e8434fba" }
    version = "4.8.0"
    name = "kdepimlibs"


    depends = ["qt4", "automoc4", "kdelibs", "gpgme", "cyrus-sasl", "akonadi",
               "shared-mime-info", "libical"]

    configure_args = [
                      "-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                      "-DKDE_DISTRIBUTION_TEXT=\"kaizen software manager\"",
                      ]
