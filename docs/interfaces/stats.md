# simpleds.stats

`simpleds.stats` is a Python 3 module that contains simple statistical 
functions for data science usage.

## Functions

### `simpleds.stats.calc_mean(collection, to_number = None)`
Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Number]` or `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
| `to_number` | `Callable[[Any], Number]` | A function that takes in any type and returns a corresponding number (`int`, `float`, or `complex`). | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The mean of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mean (e.g. empty collection, failed mapping). |
| `TypeError` | Raised if calculating mean on something other than a collection of numbers. |

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
>>> simpleds.stats.calc_mean({3, 1.0, 2, 4})
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
```python
# Calculating mean on a hybrid collection of numbers
>>> stats.calc_mean({'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5})
3.0
```

### `simpleds.stats.calc_median(collection, to_number = None)`

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Number]` or `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
| `to_number` | `Callable[[Any], Number]` | A function that takes in any type and returns a corresponding number (`int`, `float`, or `complex`). | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The median of the given collection of numbers. Returns the mean of the middle two numbers if given a collection with an even number of elements. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mean (e.g. empty collection, failed mapping). |
| `TypeError` | Raised if calculating median on something other than a collection of numbers. |

Examples:

```python
# Calculating median on a one-dimensional list of integers
>>> stats.calc_median([1, 2, 4])
2.0
```
```python
# Calculating median on an irregular n-dimensional list of floats
>>> stats.calc_median([[[1.0, 5.0], [2.0, 4.0]], [3.0]])
3.0
```
```python
# Calculating median on a set of numbers
>>> stats.calc_median({3, 1.0, 2, 4})
2.5
```
```python
# Calculating median on a dict of integers
>>> stats.calc_median({'val1': 11, 'val2': 7, 'val5': 2})
7.0
```
```python
# Calculating median on a collection of non-numbers (string-integer tuples)
>>> stats.calc_median([('val1', 11), ('val2', 7), ('val5', 2)], 
...                   lambda tup: tup[1])
7.0
```
```python
# Calculating median on a hybrid collection of numbers
>>> stats.calc_median({'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5})
3.0
```
