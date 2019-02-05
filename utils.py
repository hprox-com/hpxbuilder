import hpxqt
import os
import inspect


def get_hpqt_dir():
    return os.path.dirname(inspect.getfile(hpxqt))


def get_hprox_exec_path():
    return os.path.join(get_hpqt_dir(), "hproxy.py")


def get_hprox_media_dir_path():
    return os.path.join(get_hpqt_dir(), "media")


def get_hprox_templates_dir_path():
    return os.path.join(get_hpqt_dir(), "templates")
