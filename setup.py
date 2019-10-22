import cx_Freeze

executables =[cx_Freeze.Executable("Mechanical Keyboard Simulator.py")]

cx_Freeze.setup(
    name = 'Mechanical keyboard simulator',
    options= {"build_exe": {"packages":["pygame"], "include_files": ["fonts", "images", "sounds"]}},
     executables = executables
)