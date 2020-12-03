import cx_Freeze

executables = [cx_Freeze.Executable(
    script = "galaxy.py", icon = "assets_icon/galaxyadventure.ico")]
cx_Freeze.setup(
    name = "Galaxy Adventure",
    options = {"build_exe": {"packages": ["pygame", "pymunk"],
                            "include_files": ["assets_icon", "assets_back", "assets_faces", "assets_sounds", "assets_words"]}},
    executables = executables
)