import pytest

import simpleds.stats


#########################################
# Regression Test Inputs                #
#########################################  



#########################################
# Regression Tests                      #
#########################################

######## Public Functions ########

#### CENTRAL TENDENCY FUNCTIONS

def test_count_occurrences():
    # Counting occurrences on a one-dimensional list of integers
    assert simpleds.stats.count_occurrences([1, 2, 4]) == {1: 1, 2: 1, 4: 1}

    # Counting occurrences on an irregular n-dimensional list of floats
    assert simpleds.stats.count_occurrences(
            [[[1.0, 5.0], [2.0, 4.0]], [3.0, 2.0]]) \
        == {1.0: 1, 2.0: 2, 3.0: 1, 4.0: 1, 5.0: 1}

    # Counting occurrences on a set of numbers (sets can't have duplicates)
    assert simpleds.stats.count_occurrences({3, 1.0, 2, 1.5, 4, 1, 1}) \
        == {1.0: 1, 1.5: 1, 2.0: 1, 3.0: 1, 4.0: 1}

    # Counting occurrences on a dict of integers
    assert simpleds.stats.count_occurrences(
            {'val1': 11, 'val2': 7, 'val5': 11}) \
        == {7:1, 11: 2}

    # Counting occurrences of second values in a 2-tuple of strings
    assert simpleds.stats.count_occurrences(
            [('val1', 'x'), ('val2', 'x'), ('val5', 'y')], 
            lambda tup: tup[1]) \
        == {'x': 2, 'y': 1}

    # Counting occurrences on a flattenable, hybrid collection of numbers
    assert simpleds.stats.count_occurrences(
            {'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5}) \
        == {2.0: 3, 3.0: 1, 5.0: 1}
    
    # Counting occurrences on a flattenable, hybrid collection of values
    assert simpleds.stats.count_occurrences(
            {'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': (2, 2.0)}) \
        == {'11': 1, '2': 1, '2.0': 1, '5': 1, 'foo': 1}
    
    # Counting occurrences on an empty list
    assert simpleds.stats.count_occurrences([]) == dict()

    # Counting occurrences on an empty hybrid collection
    assert simpleds.stats.count_occurrences(
            {'val1': [], 'val2': {'v1': []}}) \
        == dict()

    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.count_occurrences('foo')

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.count_occurrences(lambda x: x)

    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.count_occurrences([1, 2], lambda x: x / 0)


def test_calc_mean():
    # Calculating mean on a one-dimensional list of integers
    assert simpleds.stats.calc_mean([1, 2, 4]) == 2.3333333333333335

    # Calculating mean on an irregular n-dimensional list of floats
    assert simpleds.stats.calc_mean([[[1.0, 5.0], [2.0, 4.0]], [3.0]]) == 3.0

    # Calculating mean on a set of numbers
    assert simpleds.stats.calc_mean({3, 1.0, 2, 4}) == 2.5

    # Calculating mean on a dict of integers
    assert simpleds.stats.calc_mean({'val1': 11, 'val2': 7, 'val5': 2}) \
        == 6.666666666666667

    # Calculating mean on a collection of non-numbers (string-integer tuples)
    assert simpleds.stats.calc_mean(
            [('val1', 11), ('val2', 7), ('val5', 2)], lambda tup: tup[1]) \
        == 6.666666666666667

    # Calculating mean on a flattenable, hybrid collection of numbers
    assert simpleds.stats.calc_mean(
            {'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5}) \
        == 3.0
    
    # Given empty collection and default float
    assert simpleds.stats.calc_mean([], default = 0.0) == 0.0

    # Given empty collection and non-float default
    with pytest.raises(ValueError):
        simpleds.stats.calc_mean([])

    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.calc_mean('foo')

    # Given a collection containing a non-number
    with pytest.raises(TypeError):
        simpleds.stats.calc_mean([1, 'foo', 2])

    # Given an flattenable collection containing a non-number
    with pytest.raises(TypeError):
        simpleds.stats.calc_mean(
            {'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': 2})

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.calc_mean(lambda x: x)
    
    # Given an empty list
    with pytest.raises(ValueError):
        simpleds.stats.calc_mean([])

    # Given a flattenable empty collection
    with pytest.raises(ValueError):
        simpleds.stats.calc_mean({'val1': [], 'val2': {'v1': [[]]}})
    
    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.calc_mean([1, 2], lambda x: x / 0)


def test_calc_median():
    # Calculating median on a one-dimensional list of integers
    assert simpleds.stats.calc_median([1, 2, 4]) == 2.0

    # Calculating median on an irregular n-dimensional list of floats
    assert simpleds.stats.calc_median([[[1.0, 5.0], [2.0, 4.0]], [3.0]]) == 3.0

    # Calculating median on a set of numbers
    assert simpleds.stats.calc_median({3, 1.0, 2, 4}) == 2.5

    # Calculating median on a dict of integers
    assert simpleds.stats.calc_median({'val1': 11, 'val2': 7, 'val5': 2}) \
        == 7.0

    # Calculating median on a collection of non-numbers (string-integer tuples)
    assert simpleds.stats.calc_median([('val1', 11), ('val2', 7), ('val5', 2)], 
                            lambda tup: tup[1]) == 7.0

    # Calculating median on a flattenable, hybrid collection of numbers
    assert simpleds.stats.calc_median(
            {'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5}) \
        == 3.0

    # Given empty collection and default float
    assert simpleds.stats.calc_median([], default = 0.0) == 0.0

    # Given empty collection and non-float default
    with pytest.raises(ValueError):
        simpleds.stats.calc_median([])
    
    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.calc_median('foo')

    # Given a collection containing a non-number
    with pytest.raises(TypeError):
        simpleds.stats.calc_median([1, 'foo', 2])

    # Given an flattenable collection containing a non-number
    with pytest.raises(TypeError):
        simpleds.stats.calc_median(
            {'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': 2})

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.calc_median(lambda x: x)
    
    # Given an empty list
    with pytest.raises(ValueError):
        simpleds.stats.calc_median([])

    # Given a flattenable empty collection
    with pytest.raises(ValueError):
        simpleds.stats.calc_median({'val1': [], 'val2': {'v1': [[]]}})

    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.calc_median([1, 2], lambda x: x / 0)


def test_calc_mode():
    # Called on a one-dimensional list of integers
    assert simpleds.stats.calc_mode([1, 2, 2, 4]) == 2

    # Called on a one-dimensional list of numbers
    assert simpleds.stats.calc_mode([1, 2, 2.0, 4, 1.0]) == 1.0

    # Called on an irregular n-dimensional list of floats
    assert simpleds.stats.calc_mode([[[1.0, 5.0], [2.0, 5.0, 4.0]], [3.0]]) == 5.0

    # Called on a set of numbers (note: sets can only contain unique elements)
    assert simpleds.stats.calc_mode({3, 1.0, 2, 2, 2, 1, 4}) == 1.0

    # Called on a dict of integers
    assert simpleds.stats.calc_mode({'val1': 11, 'val2': 7, 'val5': 11}) == 11

    # Called on second values in a 2-tuple of strings
    assert simpleds.stats.calc_mode([('val1', 'x'), ('val2', 'x'), ('val5', 'y')], 
                                   lambda tup: tup[1]) == 'x'

    # Called on a flattenable, hybrid collection of numbers
    assert simpleds.stats.calc_mode(
            {'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5}) \
        == 2.0
    
    # Called on a flattenable, hybrid collection of values
    assert simpleds.stats.calc_mode(
            {'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': (2, 2.0)}) \
        == '11'

    # Given empty collection and default float
    assert simpleds.stats.calc_mode([], default = 'empty') == 'empty'

    # Given empty collection and non-float default
    with pytest.raises(ValueError):
        simpleds.stats.calc_mode([])
    
    # Called on an empty list
    with pytest.raises(ValueError):
        simpleds.stats.calc_mode([])

    # Called on an empty hybrid collection
    with pytest.raises(ValueError):
        simpleds.stats.calc_mode({'val1': [], 'val2': {'v1': []}})

    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.calc_mode('foo')

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.calc_mode(lambda x: x)

    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.calc_mode([1, 2], lambda x: x / 0)


def test_get_range():
    # Called on a one-dimensional list of integers
    assert simpleds.stats.get_range([1, 2, 2, 4]) == (1, 4)

    # Called on a one-dimensional list of numbers
    assert simpleds.stats.get_range([1, 2, 2.0, 4, 1.0]) == (1, 4)

    # Called on a one-dimensional list of same numbers
    assert simpleds.stats.get_range([1, 1.0]) == (1, 1)

    # Called on a singleton
    assert simpleds.stats.get_range({2.0}) == (2.0, 2.0)

    # Called on an irregular n-dimensional list of floats
    assert simpleds.stats.get_range(
            [[[1.0, 5.0], [2.0, 5.0, 4.0]], [3.0]]) \
        == (1.0, 5.0)

    # Called on a set of numbers (note: sets can only contain unique elements)
    assert simpleds.stats.get_range({3, 1.0, 2, 2, 2, 1, 4}) == (1, 4)

    # Called on a dict of integers
    assert simpleds.stats.get_range({'val1': 11, 'val2': 7, 'val5': 11}) == (7, 11)

    # Called on second values in a 2-tuple of strings
    assert simpleds.stats.get_range(
            [('val1', 'x'), ('val2', 'x'), ('val5', 'y')], lambda tup: tup[1]) \
        == ('x', 'y')

    # Called on a flattenable, hybrid collection of numbers
    assert simpleds.stats.get_range(
            {'val1': 2.0, 'val2': [2.0, (3.0, 2)], 'val5': 5}) \
        == (2, 5)
    
    # Called on an empty collection, given a default
    assert simpleds.stats.get_range([], default = False) == (False, False)

    # Called on a flattenable, hybrid collection of values
    with pytest.raises(TypeError):
        simpleds.stats.get_range(
            {'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': (2, 2.0)})
    
    # Called on an empty list without a default
    with pytest.raises(ValueError):
        simpleds.stats.get_range([])

    # Called on an empty hybrid collection
    with pytest.raises(ValueError):
        simpleds.stats.get_range({'val1': [], 'val2': {'v1': []}})

    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.get_range('foo')

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.get_range(lambda x: x)

    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.get_range([1, 2], lambda x: x / 0)


#### HYPOTHESIS TESTING


#### SAMPLING

######## Private Helper Functions ########

def test___map_and_flatten_collection():
    # Called on a one-dimensional list of integers
    assert simpleds.stats.__map_and_flatten_collection([1, 2, 4]) == [1, 2, 4]

    # Called on an irregular n-dimensional list of floats
    assert simpleds.stats.__map_and_flatten_collection(
            [[[1.0, 5.0], [2.0, 4.0]], [3.0]]) == [1.0, 5.0, 2.0, 4.0, 3.0]

    # Called on a set of numbers
    assert simpleds.stats.__map_and_flatten_collection(
            {3, 1.0, 2, 4}) == [1.0, 2, 3, 4]

    # Called on a dict of integers
    assert simpleds.stats.__map_and_flatten_collection(
            {'val1': 11, 'val2': 7, 'val5': 2}) == [11, 7, 2]

    # Called on a collection of non-numbers (string-integer tuples)
    assert simpleds.stats.__map_and_flatten_collection(
            [('val1', 11), ('val2', 7), ('val5', 2)], lambda tup: tup[1]) \
        == [11, 7, 2]

    # Called on a flattenable, hybrid collection of numbers
    assert simpleds.stats.__map_and_flatten_collection(
            {'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5}) \
        == [1.0, 2.0, 3.0, 4, 5]

    # Called on a mixed collection
    assert simpleds.stats.__map_and_flatten_collection([1, 3.0, 'foo']) \
        == [1, 3.0, 'foo']
    assert simpleds.stats.__map_and_flatten_collection(
            {'a': [1.0, {'bar'}], 'b': (-2, True)}) == [1.0, 'bar', -2, True]
        
    # Given a string (collection of chars)
    with pytest.raises(TypeError):
        simpleds.stats.__map_and_flatten_collection('foo')

    # Given a non-collection
    with pytest.raises(TypeError):
        simpleds.stats.__map_and_flatten_collection(lambda x: x)
    
    # Given a bad mapping function
    with pytest.raises(ValueError):
        simpleds.stats.__map_and_flatten_collection([1, 2], lambda x : x / 0)
