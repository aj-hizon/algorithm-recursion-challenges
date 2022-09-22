#------------------------------------------------- GREATEST COMMON DIVISOR -------------------------------------------------#

# How to find GCD of two numbers using recursion?

# Another way to solve:
#   - Euclidean Algorithm

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be an integer!!"
    if a < 0:
        a = -1 * a 
    if b < 0:
        b  = -1 * b
    if b == 0:
        return a
    else: 
        return gcd(b, a%b)

print(gcd(48, 18))
