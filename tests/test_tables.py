import pytest

import simpleds.tables as tables

#########################################
# Regression Test Inputs                #
#########################################  



#########################################
# Regression Tests                      #
#########################################

######## Public Functions ########

def test_flatten():
    # Given lists
    assert list(tables.flatten([])) == []
    assert list(tables.flatten([[]])) == [] # 2d empty
    assert list(tables.flatten([[[]]])) == [] # 3d empty
    assert list(tables.flatten([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(tables.flatten([[1, 2], [3, 4]])) == [1, 2, 3, 4] # 2d
    assert list(tables.flatten([[1, 2], [3], 4])) == [1, 2, 3, 4] # 2d irreg
    assert list(tables.flatten([[[1], [2, 3]], 4])) == [1, 2, 3, 4] # 3d irreg

    # Given tuples
    assert list(tables.flatten(tuple())) == []
    assert list(tables.flatten(tuple(tuple()))) == [] # 2d empty
    assert list(tables.flatten(tuple(tuple(tuple())))) == [] # 3d empty
    assert list(tables.flatten((1, 2, 3, 4))) == [1, 2, 3, 4]
    assert list(tables.flatten(((1, 2), (3, 4)))) == [1, 2, 3, 4] # 2d
    assert list(tables.flatten(((1, 2), (3), 4))) == [1, 2, 3, 4] # 2d irreg
    assert list(tables.flatten((((1), (2, 3)), 4))) == [1, 2, 3, 4] # 3d irreg

    # Given sets -- note: can't nest sets since sets can only contain hashables
    assert list(tables.flatten(set())) == []
    assert list(tables.flatten({1, 2, 3, 4})) == [1, 2, 3, 4]

    # Given dicts
    assert list(tables.flatten(dict())) == []
    assert list(tables.flatten( {'a': dict()} )) == [] # 2d empty
    assert list(tables.flatten({'a': {'b': dict()}})) == [] # 3d empty
    assert list(tables.flatten({'a': 1, 'b': 2, 'c': 3, 'd': 4})) == [1, 2, 3, 4]
    assert list(tables.flatten({'a': {'a1': 1, 'a2': 2}, 
                                'b': {'b1': 3, 'b4': 4}})) == [1, 2, 3, 4] # 2d
    assert list(tables.flatten({'a': {'a1': 1, 'a2': 2}, 
                                'b': {'b1': 3}, 
                                'c': 4})) == [1, 2, 3, 4] # 2d irreg
    assert list(tables.flatten({'a': {'a1': {'a1a': 1}, 
                                      'a2': {'a2a': 2, 'a2b': 3}}, 
                                'b': 4})) == [1, 2, 3, 4] # 3d irreg

    # Given mixed
    assert list(tables.flatten([1, 3.0, 'foo'])) == [1, 3.0, 'foo'] # mix with string
    assert list(tables.flatten({'a': [1.0, {'bar'}], 'b': (-2, True)})) == [1.0, 'bar', -2, True]

    # Given non-iterables
    with pytest.raises(TypeError):
        list(tables.flatten('str')) == 'str' # strings perceived as a non-iterable
    with pytest.raises(TypeError):
        list(tables.flatten(lambda x : x))


######## Private Helper Functions ########


