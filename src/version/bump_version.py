from version import __version__

# Bump Version to Next Incremental and Add Snapshot: python version/bump_version.py
handler = open("./src/version/version.py", "w")
major = __version__.split(".")[0]
minor = __version__.split(".")[1]
incremental = int(__version__.split(".")[2]) + 1

handler.write(f'__version__ = "{major}.{minor}.{incremental}-SNAPSHOT"')
handler.close()

print(f"{major}.{minor}.{incremental}-SNAPSHOT")