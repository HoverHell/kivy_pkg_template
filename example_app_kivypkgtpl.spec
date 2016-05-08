# -*- mode: python -*-
"""
PyInstaller's spec files. For tuning the package build.

"""

block_cipher = None

# TODO: support other python versions:
# Either make cython use the non-version-specific library names,
# or determine the library name in runtime.
binaries = [
    # (filename, (?)name)
    ('kivypkgtplapp/hello_cython.cpython-35m-x86_64-linux-gnu.so', 'hello_cython.so'),
]
datas = [
    # (filename, target_dir)
    ('kivypkgtplapp/*.kv', 'kivypkgtplapp'),
]


# TODO: *.kv

a = Analysis(
    ['kivypkgtplapp/main.py'],
    pathex=['/home/hell/src/kivy_pkg_template'],
    binaries=binaries,
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher)
pyz = PYZ(
    a.pure, a.zipped_data,
    cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='example_app_kivypkgtpl',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='example_app_kivypkgtpl')
