import os
import platform
import tarfile

import PyInstaller.config
from PyInstaller.__main__ import run

from hpxbuilder import utils


def compress_app():
    if platform.system().lower() == 'windows':
        return

    dist_dir = os.path.join(utils.get_dist_dir(), 'dist')
    compressed_name = utils.get_compressed_name()
    compressed_fpath = os.path.join(dist_dir, '%s.tar.gz' % compressed_name)

    with tarfile.open(compressed_fpath, 'w:gz') as tar:
        arcname = os.path.join(compressed_name, 'bin',  utils.get_exec_name())
        tar.add(os.path.join(dist_dir, utils.get_exec_name()), arcname=arcname)


def process():
    PyInstaller.config.CONF['workpath'] = utils.get_dist_dir()
    run([os.path.join(utils.get_builder_base(), "win", "build.spec")])

    compress_app()


if __name__ == "__main__":
    process()
