# simpleds.stats

`simpleds.stats` is a Python 3 module that contains simple statistical 
functions for data science usage.

## Central Tendency Functions

### `simpleds.stats.calc_mean(collection, to_number = None)`
Returns the mean of a given collection.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
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
Returns the median of a given collection.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
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

### `simpleds.stats.calc_mode(collection, to_hashable = None)`
Returns the mode of a given collection. *Note*: numpy type casting applies to
return values.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of hashables. If a collection of non-hashables is provided, user can provide `to_hashable` for mapping. | *required* |
| `to_hashable` | `Callable[[Any], Hashable]` | A function that takes in any type and returns a corresponding hashable. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Hashable` | The mode of a given collection of hashables. If there's a tie, the left-most (sorted in ascending order) is returned. *Note*: numpy type casting applies to return values. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mode (e.g. empty collection, failed mapping). |
| `TypeError` | Raised if calculating mode on something other than a collection of hashables. |

Examples:

```python
# Called on a one-dimensional list of integers
>>> stats.calc_mode([1, 2, 2, 4])
2
```
```python
# Called on a one-dimensional list of numbers
>>> stats.calc_mode([1, 2, 2.0, 4, 1.0])
1.0
```
```python
# Called on an irregular n-dimensional list of floats
>>> stats.calc_mode([[[1.0, 5.0], [2.0, 5.0, 4.0]], [3.0]])
5.0
```
```python
# Called on a set of numbers (note: sets can only contain unique elements)
>>> stats.calc_mode({3, 1.0, 2, 2, 2, 1, 4})
1.0
```
```python
# Called on a dict of integers
>>> stats.calc_mode({'val1': 11, 'val2': 7, 'val5': 11})
11
```
```python
# Called on second values in a 2-tuple of strings
>>> stats.calc_mode([('val1', 'x'), ('val2', 'x'), ('val5', 'y')], 
...                 lambda tup: tup[1])
'x'
```
```python
# Called on a hybrid collection of numbers
>>> stats.calc_mode({'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5})
2.0
```
```python
# Called on a hybrid collection of values
>>> stats.calc_mode({'val1': 11, 
                     'val2': {'x': 5, 'y': 'foo'}, 
                     'val5': (2, 2.0)})
'11'
```

### `simpleds.stats.count_occurrences(collection, to_hashable = None)`

Counts the number of times a value occurs in the collection. *Note*: numpy type casting applies to returned `dict`'s keys.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of hashables. If a collection of non-hashables is provided, user can provide `to_hashable` for mapping. | *required* |
| `to_hashable` | `Callable[[Any], Hashable]` | A function that takes in any type and returns a corresponding hashable. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Dict[Hashable, int]` | A dictionary where the key is the hashable and the value is the number of times the hashable occurs in the collection. *Note*: numpy type casting applies to returned `dict`'s keys. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if given `to_hashable` fails to map. |
| `TypeError` | Raised if counting occurrences on something other than a collection of hashables. |

Examples:

```python
# Counting occurrences on a one-dimensional list of integers
>>> stats.count_occurrences([1, 2, 4])
{1: 1, 2: 1, 4: 1}
```
```python
# Counting occurrences on an irregular n-dimensional list of floats
>>> stats.count_occurrences([[[1.0, 5.0], [2.0, 4.0]], [3.0, 2.0]])
{1.0: 1, 2.0: 2, 3.0: 1, 4.0: 1, 5.0: 1}
```
``` python
# Counting occurrences on a set of numbers (sets can't have duplicates)
>>> stats.count_occurrences({3, 1.0, 2, 1.5, 4, 1, 1})
{1.0: 1, 1.5: 1, 2.0: 1, 3.0: 1, 4.0: 1}
```
```python
# Counting occurrences on a dict of integers
>>> stats.count_occurrences({'val1': 11, 'val2': 7, 'val5': 11}) \
{7:1, 11: 2}
```
```python
# Counting occurrences of second values in a 2-tuple of strings
>>> stats.count_occurrences([('val1', 'x'), ('val2', 'x'), ('val5', 'y')],
...                         lambda tup: tup[1])
{'x': 2, 'y': 1}
```
```python
# Counting occurrences on a hybrid collection of values
>>> stats.count_occurrences({'val1': 11, 
                             'val2': {'x': 5, 'y': 'foo'}, 
                             'val5': (2, 2.0)})
{'11': 1, '2': 1, '2.0': 1, '5': 1, 'foo': 1}
```


## Hypothesis Testing Functions

### `simpleds.stats.calc_margin_of_error(...)`
Coming soon.

### `simpleds.stats.calc_standard_deviation(...)`
Coming soon.

### `simpleds.stats.calc_standard_error(...)`
Coming soon.

### `simpleds.stats.conduct_chi_squared_test(...)`
Coming soon.

### `simpleds.stats.conduct_t_test(...)`
Coming soon.


## Sampling Functions

### `simpleds.stats.calc_sample_size(...)`
Coming soon.

### `simpleds.stats.calc_confidence_level(...)`
Coming soon.

