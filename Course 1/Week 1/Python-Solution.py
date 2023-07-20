def karatsuba_multiply(num1, num2):
    # Convert numbers to strings to find their lengths
    num1_str, num2_str = str(num1), str(num2)
    n1, n2 = len(num1_str), len(num2_str)

    # Base case: Single-digit multiplication
    if min(n1, n2) == 1:
        return num1 * num2

    # Split the numbers into two halves
    half_n1 = n1 // 2
    half_n2 = n2 // 2
    a, b = divmod(num1, 10 ** half_n1)
    c, d = divmod(num2, 10 ** half_n2)

    # Recursive calls for subproblems
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_bc = karatsuba_multiply(a + b, c + d) - ac - bd

    # Combine the results using the Karatsuba algorithm formula
    product = ac * 10 ** (half_n1 * 2) + ad_bc * 10 ** half_n1 + bd
    return product

# Test the function with the provided inputs
numA = 3141592653589793238462643383279502884197169399375105820974944592
numB = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba_multiply(numA, numB)
print(result)
