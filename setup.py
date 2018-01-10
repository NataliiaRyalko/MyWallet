from cx_Freeze import *

setup(
    name="MyWallet",
    version="1.4.0",
    description="MyWallet_1.4.0",
    executables=[Executable("sandbox.py")]
)
