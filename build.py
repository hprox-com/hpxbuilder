from sys import platform as _platform


def build_p2app():
    from mac import build
    build.process()


def build_pyinstaller():
    from win import build
    build.process()


if __name__ == "__main__":
    if _platform == "darwin":
        build_p2app()
    else:
        build_pyinstaller()
