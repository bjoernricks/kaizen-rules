import jam.session

class Jam(jam.session.PythonDevelopSession):

    src_path = "%(package_path)s"
    build_path = "%(package_path)s"
    version = "0.1"
    name = "jam"

    runtime_depends = ["python-bz2file"]
