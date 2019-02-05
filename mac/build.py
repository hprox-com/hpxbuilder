from setuptools import setup
from hpxbuilder import utils

def process():
    import sys
    sys.argv.append("py2app")

    APP = [utils.get_hprox_exec_path()]
    DATA_FILES = []
    PKGS = []
    OPTIONS = {
        'packages': PKGS,
        'resources': [
            utils.get_hprox_media_dir_path(),
            utils.get_hprox_templates_dir_path()]
    }

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )


if __name__ == "__main__":
    process()
