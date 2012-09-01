import kaizen.rules

from kaizen.system import Quilt

class Mysql(kaizen.rules.CMakeRules):

    url = "http://downloads.mysql.com/archives/mysql-5.5/mysql-%(version)s.tar.gz"
    hash = { "md5" : "375794ebf84b4c7b63f1676bc7416cd0",
             "sha1" : "d5066327c41ac5a338ca0bb748e50bc4e1902442" }
    version = "5.5.20"
    name = "mysql"

    depends = ["libreadline", "openssl", "zlib"]

    # patchsystem = Quilt

    configure_args = ["-DMYSQL_DATADIR=%(prefix)s/var/mysql",
                      "-DINSTALL_MYSQLSHAREDIR=%(prefix)s/share/mysql",
                      "-DINSTALL_MANDIR=%(prefix)s/share/man",
                      "-DINSTALL_INFODIR=%(prefix)s/share/info",
                      "-DINSTALL_DOCDIR=%(prefix)s/share/doc/mysql",
                      "-DINSTALL_DOCREADMEDIR=%(prefix)s/share/doc/mysql",
                      "-DINSTALL_PLUGINDIR=%(prefix)s/lib/mysql/plugin",
                      "-DINSTALL_SCRIPTDIR=%(prefix)s/share/mysql/scripts",
                      "-DINSTALL_MYSQLTESTDIR=%(prefix)s/share/mysql-test",
                      "-DINSTALL_SQLBENCHDIR=%(prefix)s/share/mysql-sql-bench",
                      "-DINSTALL_SUPPORTFILESDIR=%(prefix)s/share/support-files",
                      "-DINSTALL_INCLUDEDIR=%(prefix)s/include/mysql",
                      "-DWITH_SSL=yes",
                      "-DDEFAULT_CHARSET=utf8",
                      "-DDEFAULT_COLLATION=utf8_general_ci",
                      "-DSYSCONFDIR=%(prefix)s/etc",
                      "-DWITH_UNIT_TESTS=OFF",
                      "-DWITH_EMBEDDED_SERVER=ON",
                      "-DWITH_READLINE=yes",
                      ]
