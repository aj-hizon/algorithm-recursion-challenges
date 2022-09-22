#-------------------------------------------------------- DECIMAL TO BINARY -------------------------------------------#
# Step 1: Divide the number by 2
# Step 2: Get the integer quotient for the next iteration 
# Step 3: Get the remainder for the binary digit
# Step 4: Repeat the steps until the quotient is equal to 0

def binary(n):
    assert int(n) == n, "The number must be an integer."
    
    if n == 0:
        return 0
    else: 
        return n%2 + 10*binary(int(n/2))
    

print(binary(3069))
