"""
simpleds.tables
===============

Provides
    - Types (TypeVars and NewTypes) for data science use.

Metadata
--------
:Module:        ``simpleds.types``
:Filename:      `types.py <https://github.com/keiferc/simpleds>`_
:Author:        `@keiferc <https://github.com/keiferc>`_
:Date:          08 Feb. 2021
:Version:       0.0.0-alpha
:Description:   A Python 3 module containing types for data science.
:Contributors:  

Documentation
-------------
Documentation for ``simpleds.types`` is built using MkDocs. Run 
`mkdocs serve` to view docs.

"""
from typing import (Any, Callable, Dict, Generator, Iterable, List, Optional,
                    Set, Tuple, TypeVar, Union)


#########################################
#                                       #
#       Type Variables                  #
#                                       #
#########################################

Number = TypeVar('Number', int, float, complex)
