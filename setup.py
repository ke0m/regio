from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = """A simple package for reading and writing
                 regularly sampled datasets"""
LONG_DESCRIPTION = """A simple package for reading and writing regularly
                   sampled datasets.  Especially useful for reading
                   SEPlib.H and Madagascar .rsf files into numpy arrays"""

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="regio",
    version=VERSION,
    author="Joseph Jennings",
    author_email="<joseph29@sep.stanford.edu>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'getpass', 'datetime'],
    keywords=['python', 'hypercube', 'regularly sampled', 'regular'],
    classifiers=[
        "Intended Audience :: Seismic processing/imaging",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux ",
    ],
)
