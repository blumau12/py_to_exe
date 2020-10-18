from cx_Freeze import setup, Executable
import os

base = 'Win32GUI'    

executables = [Executable("py_project/run.py", base=base)]

packages = [
    "idna",
    "tkinter",
    "json",
    "datetime",
    "calendar",
    "requests",
    "re",
    "selenium",
    "unittest",
    "math",
]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

os.environ['TCL_LIBRARY'] = r'C:\Users\bluma\py_base_envs\python-3.7.7\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\bluma\py_base_envs\python-3.7.7\tcl\tk8.6'

setup(
    name = "<Booster payments>",
    options = options,
    version = "<1.0>",
    description = '<Clients B + 2 DB GUI management>',
    executables = executables
)
