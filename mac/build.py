from setuptools import setup
from hpxbuilder import utils

def process():
    import sys
    sys.argv.append("py2app")

    OPTIONS = {
        'argv_emulation':True,
        'packages': [],
        'resources': [
            utils.get_hprox_media_dir_path(),
            utils.get_hprox_templates_dir_path()],
        'iconfile': utils.get_app_icon_path(),
        'plist': {'CFBundleIconFile': 'icon.icns'},
    }

    setup(
        app=[utils.get_hprox_exec_path()],
        data_files=[],
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )


if __name__ == "__main__":
    process()
