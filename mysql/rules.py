import kaizen.rules

from kaizen.system import Quilt

class Mysql(kaizen.rules.CMakeRules):

    url = ["http://dev.mysql.com/get/Downloads/MySQL-5.5/mysql-%(version)s.tar.gz/from/http://cdn.mysql.com/",
           "mysql-%(version)s"]
    hash = { "md5" : "82baf46acfced6eef072e9d8a479c86e",
             "sha1" : "d53dfbe4ac1119e4c4a33d639f2904abdd0f226d" }
    version = "5.5.27"
    name = "mysql"

    depends = ["libreadline", "openssl", "zlib"]

    # patch_cmd = Quilt

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
