#!/usr/bin/python3
def weight_average(my_list=[]):
    """multiplying the tuples and diving to the total second tuples"""
    if not my_list:
        return 0
    total_num = 0
    div = 0
    for tuples in my_list:
        total_num += tuples[0] * tuples[1]
        div += tuples[1]
    return (total_num / div)
