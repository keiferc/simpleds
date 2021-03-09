import simpleds.stats as stats


#########################################
# Regression Test Inputs                #
#########################################  



#########################################
# Regression Tests                      #
#########################################
def test_calc_mean():
    assert stats.calc_mean([1, 2, 3]) == 2.0
