import glob
import sys

from setuptools import Extension, setup

source_files = ["enet.pyx"]

_enet_files = glob.glob("enet_src/*.c")

if not _enet_files:
    print("You need to download and extract the enet 1.3 source to enet_src/")
    print("Download the source from: http://enet.bespin.org/Downloads.html")
    print("See the README for more instructions")
    sys.exit(1)

source_files.extend(_enet_files)

define_macros = [
    ("HAS_POLL", None),
    ("HAS_FCNTL", None),
    ("HAS_MSGHDR_FLAGS", None),
    ("HAS_SOCKLEN_T", None),
]

libraries = []

if sys.platform == "win32":
    define_macros.append(("WIN32", None))
    libraries.extend(["ws2_32", "Winmm"])

if sys.platform != "darwin":
    define_macros.extend([("HAS_GETHOSTBYNAME_R", None), ("HAS_GETHOSTBYADDR_R", None)])

ext_modules = [
    Extension(
        "enet",
        extra_compile_args=["-O3"],
        sources=source_files,
        include_dirs=["enet_src/include/"],
        define_macros=define_macros,
        libraries=libraries,
    )
]

setup(
    ext_modules=ext_modules,
    packages=["enet"],
    package_data={"enet": ["__init__.pyi"]},
)
