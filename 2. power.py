#-------------------------------------------------- POWER --------------------------------------------------#

# How to calculate power of a number using recursion?
# x^n = x * x^n-1

#   Base - flow 
#   Stopping Criterion
#   Constraint
#       - power(-1, 2)
#       - power(3.2, 2)
#       - power(2, 1.2)
#       - power(2, -1)


def power(number, exp):
    assert exp >= 0 and int(exp) == exp, "Exponent must be greater than or equal to 0 and must be an integer!!!" 

    if exp == 0:
        return 1
    if exp == 1:
        return number
    else: 
        return number * power(number, exp-1)

print(power(number = 3.2, exp = 9.2))

