
"""
simpleds
========

Provides
    - A Python 3 module containing simple data science functions.

Metadata
--------
:Module:        ``simpleds``
:Filename:      `simpleds.py <https://github.com/keiferc/simpleds>`_
:Author:        `@keiferc <https://github.com/keiferc>`_
:Date:          08 Feb. 2021
:Version:       0.0.0-alpha
:Description:   A Python 3 module for simple data science.
:Contributors:  

Documentation
-------------
Documentation for ``simpleds`` is built using MkDocs.

"""
import pandas as pd 
import numpy as np 
import scipy as sp 

from typing import Dict, List, Set, Tuple, Union


def calc_mean(collection: Union[
                            List[Union[int, float, complex]],
                            Set[Union[int, float, complex]]]) -> float:
    if len(collection) == 0:
        raise ValueError("simpleds.calc_mean failed. Cannot calculate " + \
                         "mean on an empty collection.")
    try:
        return float(np.mean(collection))
    except TypeError:
        raise TypeError("simpleds.calc_mean failed. Cannot calculate " + \
                        "mean on a collection on non-numerical values.")


