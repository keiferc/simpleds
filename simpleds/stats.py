
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
from simpleds.types import Number, Sortable

from typing import (Any, Callable, Dict, Hashable, Iterable, List, Optional,
                    Set, Tuple, Union)


#########################################
#                                       #
#       Function Definitions            #
#                                       #
#########################################

# TODO: add `default` param to all collection functions -- value to 
# return if iterable is empty

#===========================#
# Central Tendencies        #
#===========================#

def count_occurrences(collection: Iterable[Any],
                      to_hashable: Optional[Callable[[Any], Hashable]] = None
        ) -> Dict[Hashable, int]:
    try:
        new_collection = __map_and_flatten_collection(collection, to_hashable)
    except TypeError as e:
        raise TypeError("stats.count_occurrence: {}".format(e))
    except ValueError as e:
        raise ValueError("stats.count_occurrence: {}".format(e))
    
    try:
        items, occurrences = np.unique(new_collection, return_counts = True)
        return dict(zip(items, occurrences))
    except Exception as e:
        raise TypeError("stats.count_occurrence: Cannot count occurrences " + \
                        "on '{}'. {}".format(new_collection, e))


def calc_mean(collection: Iterable[Any],
              to_number: Optional[Callable[Any, Number]] = None) -> float:
    try:
        new_collection = __map_and_flatten_collection(collection, to_number)
    except TypeError as e:
        raise TypeError("stats.calc_mean: {}".format(e))
    except ValueError as e:
        raise ValueError("stats.calc_mean: {}".format(e))

    if len(new_collection) == 0:
        raise ValueError("stats.calc_mean: Cannot calculate mean on " + \
                         "an empty collection.")

    try:
        return float(np.mean(new_collection))
    except TypeError as e:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. ".format(new_collection) + \
                        "Improper element types. {}".format(e))


def calc_median(collection: Iterable[Any],
                to_number: Optional[Callable[[Any], Number]] = None) -> float:
    try:
        new_collection = __map_and_flatten_collection(collection, to_number)
    except TypeError as e:
        raise TypeError("stats.calc_median: {}".format(e))
    except ValueError as e:
        raise ValueError("stats.calc_median: {}".format(e))

    if len(new_collection) == 0:
        raise ValueError("stats.calc_median: Cannot calculate median on " + \
                         "an empty collection.")

    try:
        return float(np.median(new_collection))
    except TypeError as e:
        raise TypeError("stats.calc_median: Cannot calculate median on " + \
                        "'{}'. ".format(new_collection) + \
                        "Improper element types. {}".format(e))


def calc_mode(collection: Iterable[Any],
              to_hashable: Optional[Callable[[Any], Hashable]] = None) -> Any:
    """
    Note: should be faster than scipy.stats.mode(...) since scipy's function
    loops per unique value (O(n^2)). TODO: test speed for verification.
    
    """
    occurrences = count_occurrences(collection, to_hashable)
    return max(occurrences, key = lambda x : occurrences[x])


def get_range(collection: Iterable[Any],
              to_sortable: Optional[Callable[[Any], Sortable]] = None,
              default: Optional[Sortable] = None) -> Tuple[Sortable, Sortable]:
    return (min(collection, to_sortable, default), 
            max(collection, to_sortable, default)) # TODO: test


#===========================#
# Hypothesis Testing        #
#===========================#

def calc_margin_of_error(collection: Iterable[Any],
                         to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    pass # TODO)


def calc_standard_deviation(collection: Iterable[Any],
                            to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    pass # TODO


def calc_standard_error(collection: Iterable[Any],
                        to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    pass # TODO


def conduct_chi_squared_test():
    pass # TODO


def conduct_t_test():
    pass # TODO


#===========================#
# Sampling                  #
#===========================#

def calc_sample_size():
    pass 


def calc_confidence_level():
    pass


#########################################
#                                       #
#       Private Function Definitions    #
#                                       #
#########################################

def __map_and_flatten_collection(collection: Iterable[Any],
                                 to_map: Optional[Callable[[Any], Any]] = None
        ) -> Iterable[Any]:
    """
    Given a collection and an optional mapping function, returns the processed 
    collection. Helper to functions that need collection prepped. 
    
    Raises 
        TypeError if given Iterable is not a flattenable Tabular post-mapping.
        ValueError if given to_map has a RuntimeError

    """
    new_collection = collection
    
    if to_map != None:
        try:
            new_collection = list(map(to_map, new_collection))
        except Exception as e:
            raise ValueError("Failed to map function " + \
                             "'{}'. {}".format(to_map, e))

    try:
        new_collection = list(tables.flatten(new_collection))
    except TypeError:
        raise TypeError("Improper format. '{}' is not a " + \
                        "Tabular.".format(collection))
    
    return new_collection

