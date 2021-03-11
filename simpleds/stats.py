
"""
simpleds.stats
==============

Provides
    - A Python 3 module containing simple statistics functions.

Metadata
--------
:Module:        ``simpleds``
:Filename:      `stats.py <https://github.com/keiferc/simpleds>`_
:Author:        `@keiferc <https://github.com/keiferc>`_
:Date:          08 Feb. 2021
:Version:       0.0.0-alpha
:Description:   A Python 3 module for simple statistics.
:Contributors:  

Documentation
-------------
Documentation for ``simpleds.stats`` is built using MkDocs. Run 
`mkdocs serve` to view docs.

"""
import pandas as pd 
import numpy as np 
import scipy as sp 

from typing import (Any, Callable, Dict, Iterable, List, Optional, 
                    Set, Tuple, TypeVar, Union)


#########################################
#                                       #
#       Type Definitions                #
#                                       #
#########################################

Number = TypeVar('Number', int, float, complex)


#########################################
#                                       #
#       Function Definitions            #
#                                       #
#########################################

def calc_mean(collection: Union[Iterable[Number], Iterable[Any]],
              to_number: Optional[Callable[Any, Number]]) -> float:
    new_collection = collection
    
    if to_number != None:
        new_collection = list(map(to_number, new_collection))

    new_collection = list(__flatten(new_collection))

    if len(new_collection) == 0:
        raise ValueError("stats.calc_mean: Cannot calculate mean on " + \
                         "an empty collection.")

    try:
        return float(np.mean(new_collection))
    except TypeError:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. Improper format.".format(collection))


#########################################
#                                       #
#       Private Function Definitions    #
#                                       #
#########################################

def __flatten(collection: Iterable[Any]) -> Iterable[Any]:
    """
    Generator that recursively flattens a given iterable. 
    
    Note: since generators return generator objects, and since strings are 
    iterables of strings, recursively returning a generator object on a string
    results in an infinite loop. This generator avoids the infinite loop by 
    treating strings as a non-iterable and thus returns the strings as is.

    """
    if isinstance(collection, str):
        raise TypeError() # tells generator to return string as is

    for item in collection: # raises TypeError is item is not an iterable
        try: 
            yield from __flatten(item) # propagates TypeError from subgenerator
        except TypeError: 
            yield item # returns item if it is not an iterable
