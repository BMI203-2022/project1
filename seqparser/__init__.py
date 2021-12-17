"""
A Python module for FAST[AQ] IO and DNA->RNA Transcribing
"""

"""
# What is an `__init__.py` file?

    The `__init__.py` file in a module is how you:
        1. specify that you are creating a python module
        2. make the submodules accessible to the user 

    It is also how to relate package specific information to
    package installers like `pip` or package distributors
    like `PyPI` and `conda`. 

# Should I write any algorithmic code here?

    No. This is meant to be a glue-type file so that your code
    can fit into other peoples code cleanly. Don't put any functions
    in here that you want other people to use. You can, but just don't. 

# Do I even need an `__init__.py` file?
    
    If you are just writing scripts in python then No. This is only used
    for when you are creating python modules that you want to call from
    other scripts or if you want to install your module to an environment.

    We hope to encourage you to modularize your code and reuse things often! 
"""

from .parse import (
        FastaParser,
        FastqParser)

from .seq import (
        transcribe,
        reverse_transcribe)

__version__ = "0.1.1"
