import hpxqt
import os
import inspect


def get_builder_base():
    return os.path.dirname(__file__)


def get_hpqt_dir():
    return os.path.dirname(inspect.getfile(hpxqt))


def get_hprox_exec_path():
    return os.path.join(get_hpqt_dir(), "hprox.py")


def get_hprox_media_dir_path():
    return os.path.join(get_hpqt_dir(), "media")


def get_hprox_templates_dir_path():
    return os.path.join(get_hpqt_dir(), "templates")


def get_app_icon_path():
    return os.path.join(get_builder_base(), 'icons', 'icon.icns')
