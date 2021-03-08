import simpleds.simpleds as sds # not pip packaged import statement


#########################################
# Regression Test Inputs                #
#########################################  



#########################################
# Regression Tests                      #
#########################################
def test_calc_mean():
    assert sds.calc_mean([1, 2, 3]) == 2.0
