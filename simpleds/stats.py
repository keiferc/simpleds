
"""
simpleds.stats
==============

Provides
    - Simple statistical functions for data science usage. 

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

import simpleds.tables as tables
from simpleds.types import Number

from typing import (Any, Callable, Dict, Hashable, Iterable, List, Optional,
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
              to_number: Optional[Callable[Any, Number]] = None) -> float:
    new_collection = collection
    
    if to_number != None:
        new_collection = list(map(to_number, new_collection))

    try:
        new_collection = list(tables.flatten(new_collection))
    except TypeError:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. Improper format.".format(collection))

    if len(new_collection) == 0:
        raise ValueError("stats.calc_mean: Cannot calculate mean on " + \
                         "an empty collection.")

    try:
        return float(np.mean(new_collection))
    except TypeError:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. Improper format.".format(collection))


def calc_median(collection: Union[Iterable[Number], Iterable[Any]],
                to_number: Optional[Callable[[Any], Number]] = None) -> float:
    new_collection = collection
    
    if to_number != None:
        new_collection = list(map(to_number, new_collection))

    try:
        new_collection = list(tables.flatten(new_collection))
    except TypeError:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. Improper format.".format(collection))

    if len(new_collection) == 0:
        raise ValueError("stats.calc_mean: Cannot calculate mean on " + \
                         "an empty collection.")

    try:
        return float(np.median(new_collection))
    except TypeError:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. Improper format.".format(collection))


# def calc_mode(collection: Iterable[Any],
#               to_map: Optional[Callable[[Any], Hashable]] = None) -> Any:
#     """
#     Note: should be faster than scipy.stats.mode(...) since scipy's function
#     loops per unique value (O(n^2)). TODO: test speed for verification.
    
#     """
#     occurrences = count_occurences(collection, to_map)
#     return max(occurrences, key = lambda x : occurrences[x])


def count_occurrences(collection: Iterable[Any],
                      to_map: Optional[Callable[[Any], Hashable]] = None
        ) -> Dict[Hashable, int]:
    pass


#########################################
#                                       #
#       Private Function Definitions    #
#                                       #
#########################################

