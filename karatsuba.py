def add(a: int, b: int) -> int:
    return a + b

def karatsuba(x, y):
    # Juts in case is one digit
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    half = n // 2 # This rounds it and floors it

    # Split x and y into two parts
    a = x // 10**half
    b = x % 10**half
    c = y // 10**half
    d = y % 10**half

    # Recursively calculate three products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(add(a, b), add(c, d)) - ac - bd

    # Combine the three products to get the final result
    result = ac * 10**(2 * half) + ab_cd * 10**half + bd

    return result
