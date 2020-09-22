from cx_Freeze import setup, Executable

execs = [Executable("main.py", icon="ourapi.icns")]
include_files = ["definitions.ini", "api_db.sqlite", "LICENSE", "README.md"]

setup(
    name="Our API",
    version="1.0",
    description="Tool for rapid API prototyping and for teaching REST/JSON with live interaction",
    options=
    {
        "build_exe":
        {
            "include_files": include_files,
            "excludes": ['tcl', 'ttk', 'tkinter', 'Tkinter']
        }
    },
    executables=execs, requires=['requests', 'PyQt5']
)
