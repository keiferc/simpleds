import simpleds.stats as stats


#########################################
# Regression Test Inputs                #
#########################################  



#########################################
# Regression Tests                      #
#########################################

######## Public Functions ########

# def test_calc_mean():
    # # Calculating mean on a one-dimensional list of integers
    # assert stats.calc_mean([1, 2, 4]) == 2.3333333333333335

    # # Calculating mean on an irregular n-dimensional list of floats
    # assert stats.calc_mean([[[1.0, 5.0], [2.0, 4.0]], [3.0]]) == 3.0

    # # Calculating mean on a set of numbers
    # assert stats.calc_mean((3, 1.0, 2, 4)) == 2.5

    # # Calculating mean on a dict of integers
    # assert stats.calc_mean({'val1': 11, 'val2': 7, 'val5': 2}) \
    #     == 6.666666666666667

    # # Calculating mean on a collection of non-numbers (string-integer tuples)
    # assert stats.calc_mean([('val1', 11), ('val2', 7), ('val5', 2)], 
    #                         lambda tup: tup[1]) == 6.666666666666667

    # # Calculating mean on a flattenable, hybrid collection of numbers
    # assert stats.calc_mean({'val1': 1.0, 'val2': [2.0, (3.0, 4)], 'val5': 5}) \
    #     == 3.0
    
    # # Given a string (collection of chars)
    # with pytest.raises(TypeError):
    #     stats.calc_mean('foo')

    # # Given a collection containing a non-number
    # with pytest.raises(TypeError):
    #     stats.calc_mean([1, 'foo', 2])

    # # Given an flattenable collection containing a non-number
    # with pytest.raises(TypeError):
    #     stats.calc_mean({'val1': 11, 'val2': {'x': 5, 'y': 'foo'}, 'val5': 2})

    # # Given a non-collection
    # with pytest.raises(TypeError):
    #     stats.calc_mean(lambda x: x)
    
    # # Given an empty list
    # with pytest.raises(ValueError):
    #     stats.calc_mean([])

    # # Given a flattenable empty collection
    # with pytest.raises(ValueError):
    #     stats.calc_mean({'val1': [], 'val2': {'v1': [[]]}})


######## Private Helper Functions ########


