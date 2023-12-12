'''
Modbus Simu App
===============
'''

import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('C:\\dev_env\\Python\\Python3608\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('C:\\dev_env\\Python\\Python3608\\share\\sdl2\\bin')

import click
import sys
import six

if six.PY2:
    import __builtin__
else:
    import builtins as __builtin__


@click.command()
@click.option("-p", is_flag=True, help="use pymodbus as modbus backend")
def _run(p):
    __builtin__.USE_PYMODBUS = p
    if "-p" in sys.argv:
        # cleanup before kivy gets confused
        sys.argv.remove("-p")
    from modbus_simulator.ui.gui import run
    run()


if __name__ == "__main__":
    _run()
