# simpleds.tables

`simpleds.tables` is a Python 3 module that contains functions for operating
on data tables (e.g. dataframes, ndarrays, iterables).


## Functions

### `simpleds.tables.flatten(collection)`
A generator that recursively flattens a given collection. *Note*: this 
function treats strings as non-iterables.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of values. | *required* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Generator` | A generator that yields the next flattened element in the given collection. |

Raises:

| Error | Description |
| ---- | ----------- |
| `TypeError` | Raised if given a non-iterable. *Note*: this function treats strings as non-iterables.|

Examples:

```python
# Flattening an irregular multi-dimensional list of integers
>>> list(tables.flatten([[[1], [2, 3]], 4]))
[1, 2, 3, 4]
```
```python
# Flattening an irregular multi-dimensional collection of mixed values
>>> list(tables.flatten({'a': [1.0, {'bar'}], 'b': (-2, True)}))
[1.0, 'bar', -2, True]
```
