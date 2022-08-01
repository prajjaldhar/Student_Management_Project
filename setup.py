import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Prajjal\AppData\Local\Programs\Python\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Prajjal\AppData\Local\Programs\Python\Python36\tcl\tk8.6"

executables = [cx_Freeze.Executable("Hostel_Management_Cgec_V1.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Hostel Management Cgec",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico", 'tcl86t.dll', 'tk86t.dll', 'images', 'database']}},
    version = "1.0",
    description = "Hostel Management Cgec| Developed By Prajjal Dhar",
    executables = executables
    )