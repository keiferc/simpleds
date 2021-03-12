"""
simpleds.tables
===============

Provides
    - Functions that operate on data tables.

Metadata
--------
:Module:        ``simpleds.tables``
:Filename:      `tables.py <https://github.com/keiferc/simpleds>`_
:Author:        `@keiferc <https://github.com/keiferc>`_
:Date:          08 Feb. 2021
:Version:       0.0.0-alpha
:Description:   A Python 3 module for data table operations.
:Contributors:  

Documentation
-------------
Documentation for ``simpleds.tables`` is built using MkDocs. Run 
`mkdocs serve` to view docs.

"""
import pandas as pd 
import numpy as np 
import scipy as sp 

from simpleds.types import Tabular

from typing import Any, Dict, Generator, Iterable


#########################################
#                                       #
#       Function Definitions            #
#                                       #
#########################################

def flatten(collection: Tabular) -> Generator:
    """
    Note: since generators return generator objects, and since strings are 
    iterables of strings, recursively returning a generator object on a string
    results in an infinite loop. This generator avoids the infinite loop by 
    treating strings as a non-iterable and thus returns the strings as is.

    """
    if isinstance(collection, str):
        raise TypeError() # tells generator to return string as is
    
    for item in collection: # raises TypeError is item is not an iterable
        try: # propagates TypeError from subgenerator
            if isinstance(collection, dict):
                yield from flatten(collection[item])
            else:
                yield from flatten(item) 
        except TypeError: # returns item if it is not an iterable
            if isinstance(collection, dict):
                yield collection[item]
            else:
                yield item 


#########################################
#                                       #
#       Private Function Definitions    #
#                                       #
#########################################


