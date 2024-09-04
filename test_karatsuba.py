from karatsuba import add, karatsuba

# Example usage with 64-digit numbers
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2

def test_base_case():
    assert karatsuba(9, 9) == 81

def test_n_is_2_case():
    assert karatsuba(10, 10) == 100

def test_n_is_4_case():
    assert karatsuba(1000, 1000) == 1000000

def test_n_is_64_case():
    assert karatsuba(x, y) == x * y

def test_n_is_3_case():
    assert karatsuba(100, 100) == 10000

def test_n_is_5_case():
    assert karatsuba(10000, 10000) == 100000000