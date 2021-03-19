"""
simpleds.stats
==============

Provides
    - Simple statistical functions for data science usage. 

Metadata
--------
:Module:        ``simpleds.stats``
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
import scipy

import simpleds.tables as tables
from simpleds.dstypes import Number, Sortable

from typing import (Any, Callable, Dict, Hashable, Iterable, List, Optional,
                    Set, Tuple, Union)


#########################################
#                                       #
#       Function Definitions            #
#                                       #
#########################################

#===========================#
# Central Tendencies        #
#===========================#

def count_occurrences(collection: Iterable[Any],
                      to_hashable: Optional[Callable[[Any], Hashable]] = None
        ) -> Dict[Hashable, int]:
    try:
        new_collection = __map_and_flatten_collection(collection, to_hashable)
    except Exception as e:
        e.args = ("stats.count_occurrences: {}".format(e),)
        raise
    
    items, occurrences = np.unique(new_collection, return_counts = True)
    return dict(zip(items, occurrences))


def calc_mean(collection: Iterable[Any],
              to_number: Optional[Callable[Any, Number]] = None,
              default: Optional[float] = None) -> float:
    try:
        new_collection = __map_and_flatten_collection(collection, to_number)
    except Exception as e:
        e.args = ("stats.calc_mean: {}".format(e),)
        raise

    if len(new_collection) == 0:
        if isinstance(default, float):
            return default
        raise ValueError("stats.calc_mean: Cannot calculate mean on " + \
                         "an empty collection.")

    try:
        return float(np.mean(new_collection))
    except TypeError as e:
        raise TypeError("stats.calc_mean: Cannot calculate mean on " + \
                        "'{}'. ".format(new_collection) + \
                        "Improper element types. {}".format(e))


def calc_median(collection: Iterable[Any],
                to_number: Optional[Callable[[Any], Number]] = None,
                default: Optional[float] = None) -> float:
    try:
        new_collection = __map_and_flatten_collection(collection, to_number)
    except Exception as e:
        e.args = ("stats.calc_median: {}".format(e),)
        raise

    if len(new_collection) == 0:
        if isinstance(default, float):
            return default
        raise ValueError("stats.calc_median: Cannot calculate median on " + \
                         "an empty collection.")

    try:
        return float(np.median(new_collection))
    except TypeError as e:
        raise TypeError("stats.calc_median: Cannot calculate median on " + \
                        "'{}'. ".format(new_collection) + \
                        "Improper element types. {}".format(e))


def calc_mode(collection: Iterable[Any],
              to_hashable: Optional[Callable[[Any], Hashable]] = None,
              default: Optional[Hashable] = None) -> Hashable:
    """
    Note: should be faster than scipy.stats.mode(...) since scipy's function
    loops per unique value (O(n^2)). TODO: test speed for verification.
    
    """
    occurrences = count_occurrences(collection, to_hashable)

    try:
        if default == None:
            return max(occurrences, key = lambda x : occurrences[x])
        return max(occurrences, key = lambda x : occurrences[x], 
                   default = default)
    except ValueError:
        raise ValueError("stats.calc_mode: Cannot calculate mode on an " + \
                         "empty collection.")


def get_range(collection: Iterable[Any],
              to_sortable: Optional[Callable[[Any], Sortable]] = None,
              default: Optional[Sortable] = None) -> Tuple[Sortable, Sortable]:
    try:
        new_collection = __map_and_flatten_collection(collection, to_sortable)
    except Exception as e:
        e.args = ("stats.get_range: {}".format(e),)
        raise

    try:
        if default == None:
            return (min(new_collection), max(new_collection)) 
        else:
            return (min(new_collection, default = default), 
                    max(new_collection, default = default))
            
    except ValueError:
       raise ValueError("stats.get_range: Cannot get range of an empty " + \
                        "collection.")


#===========================#
# Hypothesis Testing        #
#===========================#

def calc_standard_deviation(collection: Iterable[Any],
                            to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    """
    Returns standard deviation (dispersion of values from mean). Used as a
    measure of data variability. Convenience wrapper of numpy.std() on
    evaluation ratings.

    """
    pass # TODO: np.std


def calc_standard_error(collection: Iterable[Any],
                        to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    """
    Returns standard error of the mean (distance of sample mean to true
    mean). Used as a measure of accuracy of sample mean.

    """
    pass # TODO: np.sem


def calc_t_score():
    pass # TODO: scipy.stats.t.ppf


def calc_z_score():
    pass # TODO: scipy.stats.zscore


def calc_margin_of_error(collection: Iterable[Any],
                         to_number: Optional[Callable[[Any], Number]] = None
        ) -> float:
    """
    Given a confidence level, returns the margin of error (half-width of
    confidence interval of a sample mean). Used as an indicator of the
    range in which a replicated experiment mean would lie.

    Uses t-values for small samples (n < 30) and z-values for large samples
    (n >= 30).

    """
    # TODO: scipy.stats.norm.interval() if len(collection) < 30
    # TODO: scipy.stats.t.interval() if len(collection) >= 30


def conduct_chi_squared_test():
    pass # TODO: scipy.stats.chi2_contingency


def conduct_t_test():
    pass # TODO: scipy.stats.ttest_*


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
        raise TypeError("Improper format. '{}' ".format(collection) + \
                        "is not a simpleds.dstypes.Tabular.")
    
    return new_collection

