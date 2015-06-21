"""IPyMol: View and control your PyMol sessions from the IPython Notebook.
"""

from setuptools import setup, find_packages


classifiers = """\
    Development Status :: 3 - Alpha
    Intended Audience :: Science/Research
    License :: OSI Approved :: Apache Software License
    Programming Language :: Python
    Programming Language :: Python :: 2.6
    Programming Language :: Python :: 2.7
    Operating System :: Unix
    Operating System :: MacOS
    Operating System :: Microsoft :: Windows
    Topic :: Scientific/Engineering"""

setup(
    name="ipymol",
    version="0.1",
    packages=find_packages(),
    scripts=[],
    zip_safe=True,
    platforms=["Windows", "Linux", "Mac OS-X", "Unix"],
    classifiers=[e.strip() for e in classifiers.splitlines()],
    author="Carlos Xavier Hernández",
    author_email="cxh@stanford.edu",
    description=("View and control your PyMol sessions from "
                 "the IPython Notebook."),
    license="MIT",
    keywords="protein molecular visualization",
    url="http://github.com/cxhernandez/ipymol"
)
