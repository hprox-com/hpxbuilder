import platform

import hpxqt
import os
import inspect


def get_builder_base():
    return os.path.dirname(__file__)


def get_dist_dir():
    return os.path.dirname(get_builder_base())


def get_hpxqt_version():
    return hpxqt.__version__


def get_compressed_name():
    _os = platform.system().lower()
    compressed_name_map = {
        'darwin': 'hprox-{version}-osx',
        'linux': 'hprox-{version}-x86_64-linux-gnu'
    }
    return compressed_name_map[_os].format(version=get_hpxqt_version())


def get_exec_name():
    if platform.system().lower() == 'windows':
        return 'hprox-{version}-win64'.format(version=get_hpxqt_version())
    return 'hprox'


def get_hpqt_dir():
    return os.path.dirname(inspect.getfile(hpxqt))


def get_hprox_exec_path():
    return os.path.join(get_hpqt_dir(), "hprox.py")


def get_hprox_media_dir_path():
    return os.path.join(get_hpqt_dir(), "media")


def get_hprox_templates_dir_path():
    return os.path.join(get_hpqt_dir(), "templates")


def get_app_icon_path():
    _os = platform.system().lower()
    icons_map = {
        'darwin': 'icon.icns',
        'windows': 'icon.ico',
        'linux': 'icon.png'
    }
    return os.path.join(get_builder_base(), 'icons', icons_map[_os])
