import os
import platform
from pathlib import Path

from . import main
from .color_util import printc


def run_py():
    try:
        main.run()
    except KeyboardInterrupt:
        printc('&cThe program is interrupted by ^C, exiting...')
        exit(0)


def run_rust():
    # Find the rust executable
    pd = Path(__file__).parent.joinpath('rust')
    pd = pd.joinpath('hyfetch.exe' if platform.system() == 'Windows' else 'hyfetch')
    if not pd.exists():
        printc('&cThe rust executable is not found, falling back to python...')
        run_py()
        return

    # Run the rust executable
    os.system(str(pd))


if __name__ == '__main__':
    run_py()
