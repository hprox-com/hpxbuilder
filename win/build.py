import os

from PyInstaller.__main__ import run

from hpxbuilder import utils


def process():
    run([os.path.join(utils.get_builder_base(), "win", "build.spec")])


if __name__ == "__main__":
    process()
