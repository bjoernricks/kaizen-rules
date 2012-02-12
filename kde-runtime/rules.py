import jam.session

class Kderuntime(jam.session.CMakeSession):

    url = "ftp://ftp.kde.org/pub/kde/stable/4.8.0/src/kde-runtime-4.8.0.tar.bz2"
    hash = { "md5" : "571563f6ab330348d3f917abdf9c69e4",
             "sha1" : "5e1e98535529a67f8d20e8c76d051c81604d7064" }
    version = "4.8.0"
    name = "kde-runtime"

    depends = ["kdelibs", "soprano", "shared-desktop-ontologies", "soprano",
               "virtuoso", "redland", "raptor2", "attica", "xz",
               "shared-mime-info", "libjpeg"]

    configure_args = [
                      "-DBUNDLE_INSTALL_DIR=%(apps_dir)s/KDE4",
                      "-DKDE_DISTRIBUTION_TEXT=\"jam software manager\"",
                      ]
