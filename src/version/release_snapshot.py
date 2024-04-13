from version import __version__

# Release Snapshot: python version/release_snapshot.py
handler = open("./src/version/version.py", "w")
released_version = __version__.split("-")[0]
handler.write(f'__version__ = "{released_version}"')
handler.close()

print(released_version)