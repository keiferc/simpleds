# simpleds.stats

`simpleds.stats` is a Python 3 module that contains simple statistical 
functions for data science usage.

## Functions

### `simpleds.stats.calc_mean(collection)`
Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Number]` or `Iterable[Any]` | An n-dimensional collection of numbers. If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
| `to_number` | `Callable[Any, Number]` | A function that takes in any type and returns a corresponding number. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The mean of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if calculating mean on an empty collection. |
| `TypeError` | Raised if calculating mean on non-collection of numbers. |

Examples:

```python
# Calculating mean on a one-dimensional list of integers
>>> simpleds.stats.calc_mean([1, 2, 4])
2.3333333333333335
```
```python
# Calculating mean on an irregular n-dimensional list of floats
>>> simpleds.stats.calc_mean([[[1.0, 5.0], [2.0, 4.0]], [3.0]])
3.0
```
```python
# Calculating mean on a set of numbers
>>> simpleds.stats.calc_mean((3, 1.0, 2, 4))
2.5
```
```python
# Calculating mean on a dict of integers
>>> simpleds.stats.calc_mean({'val1': 11, 'val2': 7, 'val5': 2})
6.666666666666667
```
```python
# Calculating mean on a collection of non-numbers (string-integer tuples)
>>> simpleds.stats.calc_mean([('val1', 11), ('val2', 7), ('val5', 2)],
...                          lambda tup: tup[1])
6.666666666666667
```

### `simpleds.stats.calc_median(collection)`

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `List[number]` or `Set[number]`| A one-dimensional collection of numbers. | *required* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The median of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Error | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate median of the given collection. |
| `TypeError` | Raised if given a collection of non-numerical values. |

Examples:

```python
>>> simpleds.stats.calc_median([1, 2, 4])
2.0
```
```python
>>> simpleds.stats.calc_median([3, 1, 2, 4])
2.5
```
```python
>>> simpleds.stats.calc_median((3, 1.0, 2, 4))
2.5
```
