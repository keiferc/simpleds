# simpleds.stats

`simpleds.stats` is a Python 3 module that contains simple statistical 
functions for data science usage.

## Central Tendency Functions

### `calc_mean(collection, to_number = None, default = None)`
Returns the mean of a given collection.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
| `to_number` | `Callable[[Any], Number]` | A function that takes in any type and returns a corresponding number (`int`, `float`, or `complex`). | *optional* |
| `default` | `float` | A value that is returned if attempting to calculate mean on an empty collection. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The mean of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mean (e.g. empty collection without default, failed mapping). |
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
>>> simpleds.stats.calc_mean({'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5})
3.0
```
```python
# Calculating mean on an empty collection, given a float default
>>> simpleds.stats.calc_mean([], default = 0.0)
0.0
```


### `calc_median(collection, to_number = None, default = None)`
Returns the median of a given collection.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of numbers (`int`, `float`, or `complex`). If a collection of non-numbers is provided, user can provide `to_number` for mapping. | *required* |
| `to_number` | `Callable[[Any], Number]` | A function that takes in any type and returns a corresponding number (`int`, `float`, or `complex`). | *optional* |
| `default` | `float` | A value that is returned if attempting to calculate median on an empty collection. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The median of the given collection of numbers. Returns the mean of the middle two numbers if given a collection with an even number of elements. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mean (e.g. empty collection without default, failed mapping). |
| `TypeError` | Raised if calculating median on something other than a collection of numbers. |

Examples:

```python
# Calculating median on a one-dimensional list of integers
>>> simpleds.stats.calc_median([1, 2, 4])
2.0
```
```python
# Calculating median on an irregular n-dimensional list of floats
>>> simpleds.stats.calc_median([[[1.0, 5.0], [2.0, 4.0]], [3.0]])
3.0
```
```python
# Calculating median on a set of numbers
>>> simpleds.stats.calc_median({3, 1.0, 2, 4})
2.5
```
```python
# Calculating median on a dict of integers
>>> simpleds.stats.calc_median({'val1': 11, 'val2': 7, 'val5': 2})
7.0
```
```python
# Calculating median on a collection of non-numbers (string-integer tuples)
>>> simpleds.stats.calc_median([('val1', 11), ('val2', 7), ('val5', 2)], 
...                            lambda tup: tup[1])
7.0
```
```python
# Calculating median on a hybrid collection of numbers
>>> simpleds.stats.calc_median({'val1': 1.0, 'val2': [2, (3.0, 4)], 'val5': 5})
3.0
```
```python
# Calculating median on an empty collection, given a float default
>>> simpleds.stats.calc_median([], default = 0.0)
0.0
```


### `calc_mode(collection, to_hashable = None, default = None)`
Returns the mode of a given collection. *Note*: numpy type casting applies to
return values.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of hashables. If a collection of non-hashables is provided, user can provide `to_hashable` for mapping. | *required* |
| `to_hashable` | `Callable[[Any], Hashable]` | A function that takes in any type and returns a corresponding hashable. | *optional* |
| `default` | `Hashable` | A hashable that is returned if attempting to calculate mode on an empty collection. | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Hashable` | The mode of a given collection of hashables. If there's a tie, the left-most (sorted in ascending order) is returned. *Note*: numpy type casting applies to return values. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if unable to calculate mode (e.g. empty collection without default, failed mapping). |
| `TypeError` | Raised if calculating mode on something other than a collection of hashables. |

Examples:

```python
# Called on a one-dimensional list of integers
>>> simpleds.stats.calc_mode([1, 2, 2, 4])
2
```
```python
# Called on a one-dimensional list of numbers
>>> simpleds.stats.calc_mode([1, 2, 2.0, 4, 1.0])
1.0
```
```python
# Called on an irregular n-dimensional list of floats
>>> simpleds.stats.calc_mode([[[1.0, 5.0], [2.0, 5.0, 4.0]], [3.0]])
5.0
```
```python
# Called on a set of numbers (note: sets can only contain unique elements)
>>> simpleds.stats.calc_mode({3, 1.0, 2, 2, 2, 1, 4})
1.0
```
```python
# Called on a dict of integers
>>> simpleds.stats.calc_mode({'val1': 11, 'val2': 7, 'val5': 11})
11
```
```python
# Called on second values in a 2-tuple of strings
>>> simpleds.stats.calc_mode([('val1', 'x'), ('val2', 'x'), ('val5', 'y')], 
...                          lambda tup: tup[1])
'x'
```
```python
# Called on a hybrid collection of numbers
>>> simpleds.stats.calc_mode({'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5})
2.0
```
```python
# Called on a hybrid collection of values
>>> simpleds.stats.calc_mode({'val1': 11, 
...                  'val2': {'x': 5, 'y': 'foo'}, 
...                  'val5': (2, 2.0)})
'11'
```
```python
# Called on an empty list, given a default
>>> simpleds.stats.calc_mode([], default = 'empty')
'empty'
```


### `count_occurrences(collection, to_hashable = None)`
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
>>> simpleds.stats.count_occurrences([1, 2, 4])
{1: 1, 2: 1, 4: 1}
```
```python
# Counting occurrences on an irregular n-dimensional list of floats
>>> simpleds.stats.count_occurrences([[[1.0, 5.0], [2.0, 4.0]], [3.0, 2.0]])
{1.0: 1, 2.0: 2, 3.0: 1, 4.0: 1, 5.0: 1}
```
``` python
# Counting occurrences on a set of numbers (sets can't have duplicates)
>>> simpleds.stats.count_occurrences({3, 1.0, 2, 1.5, 4, 1, 1})
{1.0: 1, 1.5: 1, 2.0: 1, 3.0: 1, 4.0: 1}
```
```python
# Counting occurrences on a dict of integers
>>> simpleds.stats.count_occurrences({'val1': 11, 'val2': 7, 'val5': 11})
{7:1, 11: 2}
```
```python
# Counting occurrences of second values in a 2-tuple of strings
>>> simpleds.stats.count_occurrences([('v1', 'x'), ('v2', 'x'), ('v5', 'y')],
...                                  lambda tup: tup[1])
{'x': 2, 'y': 1}
```
```python
# Counting occurrences on a hybrid collection of values
>>> simpleds.stats.count_occurrences({'val1': 11, 
...                                   'val2': {'x': 5, 'y': 'foo'}, 
...                                   'val5': (2, 2.0)})
{'11': 1, '2': 1, '2.0': 1, '5': 1, 'foo': 1}
```


### `get_range(collection, to_sortable = None, default = None)`
Returns the inclusive range of the flattened given collection in 2-tuple 
form. Minimum value on the left. Maximum value on the right.

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `Iterable[Any]` | An n-dimensional collection of sortables. If a collection of non-sortables is provided, user can provide `to_sortable` for mapping. | *required* |
| `to_sortable` | `Callable[[Any], Sortable]` | A function that takes in any type and returns a corresponding Sortable (i.e. a value on which a relational comparator can be used). | *optional* |
| `default` | `Sortable` | A value to return for each element in the tuple if they cannot be found (e.g. due to having given an empty collection). | *optional* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `Tuple[Sortable, Sortable]` | A 2-tuple where the left is the minimum value and the right is the maximum value. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if given `to_sortable` fails to map. |
| `TypeError` | Raised if attempting to get range on a collection of non-sortable values. |

Examples:

```python
# Called on a one-dimensional list of integers
>>> simpleds.stats.get_range([1, 2, 2, 4])
(1, 4)
```
```python
# Called on a one-dimensional list of numbers
>>> simpleds.stats.get_range([2, 2.0, 4, 1.0])
(1.0, 4)
```
```python
# Called on a one-dimensional list of same-value numbers
>>> simpleds.stats.get_range([1, 1.0])
(1, 1)
```
```python
# Called on a singleton
>>> simpleds.stats.get_range({2.0})
(2.0, 2.0)
```
```python
# Called on an irregular n-dimensional list of floats
>>> simpleds.stats.get_range([[[1.0, 5.0], [2.0, 5.0, 4.0]], [3.0]])
(1.0, 5.0)
```
```python
# Called on a set of number 
>>> simpleds.stats.get_range({3, 1.0, 2, 2, 2, 1, 4})
(1, 4)
```
```python
# Called on a dict of integers
>>> simpleds.stats.get_range({'val1': 11, 'val2': 7, 'val5': 11})
(7, 11)
```
```python
# Called on second values in a 2-tuple of strings
>>> simpleds.stats.get_range([('val1', 'x'), ('val2', 'x'), ('val5', 'y')], 
...                          lambda tup: tup[1])
('x', 'y')
```
```python
# Called on a n-dimensional hybrid collection of numbers
>>> simpleds.stats.get_range({'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5})
(2, 5)
```
```python
# Called on an empty list, given a default
>>> simpleds.stats.get_range([], default = False)
(False, False)
```

## Hypothesis Testing Functions

### `calc_margin_of_error(...)`
Coming soon.

### `calc_standard_deviation(...)`
Coming soon.

### `calc_standard_error(...)`
Coming soon.

### `conduct_chi_squared_test(...)`
Coming soon.

### `conduct_t_test(...)`
Coming soon.


## Sampling Functions

### `calc_sample_size(...)`
Coming soon.

### `calc_confidence_level(...)`
Coming soon.

