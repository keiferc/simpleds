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

    # Given sets
    assert list(tables.flatten(set())) == []
    assert list(tables.flatten(set(set()))) == [] # 2d empty
    assert list(tables.flatten(set(set(set())))) == [] # 3d empty
    assert list(tables.flatten((1, 2, 3, 4))) == [1, 2, 3, 4]
    assert list(tables.flatten(((1, 2), (3, 4)))) == [1, 2, 3, 4] # 2d
    assert list(tables.flatten(((1, 2), (3), 4))) == [1, 2, 3, 4] # 2d irreg
    assert list(tables.flatten((((1), (2, 3)), 4))) == [1, 2, 3, 4] # 3d irreg

    # Given dicts


    # Given strings
    assert list(tables.flatten([1, 3.0, 'foo'])) == [1, 3.0, 'foo'] # mix with string


    # Given non-iterables
    

######## Private Helper Functions ########


