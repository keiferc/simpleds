# simpleds.stats

This page contains the function contracts for all public functions in 
`simpleds.stats`.

### `simpleds.stats.calc_mean(collection)`

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `List[number]` or `Set[number]`| A collection of numbers | *required* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The mean of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
| ---- | ----------- |
| `ValueError` | Raised if given an empty collection. |
| `TypeError` | Raised if given a collection of non-numerical values. |

Examples:

```python
>>> simpleds.stats.calc_mean([1, 2, 4])
2.3333333333333335
```
```python
>>> simpleds.stats.calc_mean([3, 1, 2, 4])
2.5
```
```python
>>> simpleds.stats.calc_mean((3, 1.0, 2, 4))
2.5
```


### `simpleds.stats.calc_median(collection)`

Parameters:

| Name | Type | Description | Default |
| ---- | ---- | ----------- | ------- |
| `collection` | `List[number]` or `Set[number]`| A collection of numbers | *required* |

Returns:

| Type | Description |
| ---- | ----------- | 
| `float` | The median of the given collection of numbers. *Note*: Python 3 floating point precision errors apply. |

Raises:

| Type | Description |
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
