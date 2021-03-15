# simpleds.dstypes

`simpleds.dstypes` is a Python 3 module that contains types (TypeVars and
NewTypes) for data science operations. Primarily used for convenient type 
hinting and checking.


## Type Aliases

### `simpleds.dstypes.Number`
An `int`, a `float`, or a `complex`.

### `simpleds.dstypes.Sortable`
Refers to types/objects that support relational operators. Current 
implementation supports `Number` and `str`. Robust implementation
support `__lt__`, `__le__`, etc. coming soon.

### `simpleds.dstypes.Tabular`
A collection that can be used as a data table. Refers to any one of Python's 
built-in container types: `list`, `set`, `tuple`, and `dict`.
