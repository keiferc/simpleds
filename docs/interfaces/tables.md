# simpleds.tables

`simpleds.tables` is a Python 3 module that contains functions for operating
on data tables (e.g. dataframes, ndarrays, iterables).


## Functions

### `simpleds.tables.flatten(collection)`
A generator that recursively flattens a given collection.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Number]` or `Iterable[Any]` | An n-dimensional collection of numbers. If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Generator` | A generator that yields the next flattened element in the given collection. |

Examples:

```python
# Calculating mean on a one-dimensional list of integers # TODO
>>> simpleds.stats.calc_mean([1, 2, 4])
2.3333333333333335
```
