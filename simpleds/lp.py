
"""
simpleds.lp
===========

Provides
    - Simple functions for linear programming

Metadata
--------
:Module:        ``simpleds.lp``
:Filename:      `lp.py <https://github.com/keiferc/simpleds>`_
:Author:        `@keiferc <https://github.com/keiferc>`_
:Date:          08 Feb. 2021
:Version:       0.0.0-alpha
:Description:   A Python 3 module for simple linear programming.
:Contributors:  

Documentation
-------------
Documentation for ``simpleds.lp`` is built using MkDocs. Run 
`mkdocs serve` to view docs.

"""
import pandas as pd 
import numpy as np 
import scipy as sp

from typing import Any, Callable, Iterable, Optional


#########################################
#                                       #
#       Function Definitions            #
#                                       #
#########################################

#===========================#
# Descriptive Functions     #
#===========================#

def calc_percent_satisfiable(collection: Iterable[Any],
                             to_map: Optional[Callable[[Any], Any]] = None,
                             constraints: Iterable[Callable[[Any], bool]] = []
    ) -> float:
    """
    Returns the number of elements / the total number of elements in the collection
    that satisfies the given collection of constraints.

    """
    pass # TODO
