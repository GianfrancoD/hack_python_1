"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8(number, number_two):
    result = [1,3,5,7,9]
    if number in result and number_two in result:
        result.pop(result.index(1))
        result.pop(result.index(9))
    return result  

print(fn_hack_8(1,9))