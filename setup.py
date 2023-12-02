"""
Clinical Pipeline Skeleton (CLPI)
"""
import os
from distutils.core import setup

from clpi.version import version

__version__ = version


def pip_requirements():
    with open("requirements.pip") as fp:
        requirements = [line.strip() for line in fp.readlines()]
    if os.path.exists("requirements_config.pip"):
        with open("requirements_config.pip") as fp:
            requirements += [line.strip() for line in fp.readlines()]

    return requirements


setup(
    author="Horatio FM",
    author_email="horatio.fm@gmail.com",
    description="Clinical Pipeline Skeleton",
    long_description=__doc__,
    fullname="Clinical Pipeline Skeleton (CPS)",
    name="clpipe",
    python_requires='>=3.10',
    url="",
    version=__version__.split("-")[0],
    platforms=["Linux"],
    packages=[
        "clpi",
        "clpi.bin"
    ],
    install_requires=pip_requirements(),
    entry_points={
        'console_scripts': [
            "clpi=clpi.bin.clpi_main:main",
            "autoclpi=clpi.bin.auto_clpi_main:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Server Environment",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python",
    ]
)
