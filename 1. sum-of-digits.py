
# sum of digits using iteration 
def sum_using_iteration(n:int): 
    stringed = str(n)
    numbers = [int(n) for n in stringed]
    return sum(numbers)

print(sum_using_iteration(12))
    


#--------------------------------SUM OF DIGITS------------------------------#

# How to find the sum of digits of a positive integer number using recursion?
#f(n) = n%10 + f(n/10)

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "Number must be greater than 0"
    if n == 0:
        return n
    else:
        return int(n%10) + sum_of_digits(int(n/10))

print(sum_of_digits(1111111)) 



