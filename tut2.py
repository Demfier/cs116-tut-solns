# This file contains solutions to CS116, Tutorial 1
import check

# CQ1: f(3) => None as none of the if conditions would be triggered


def is_triangle(s1, s2, s3):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    longest = max(s1, s2, s3)
    shortest = min(s1, s2, s3)
    mid = s1 + s2 + s3 - (longest + shortest)

    if longest > shortest + mid:
        return "No Triangle exists"
    elif longest == shortest + mid:
        return "A degenerate triangle exists"
    else:
        return "Triangle exists"


# Tests for is_triangle go here


def fermat_check(a, b, c, n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if n == 2:
        if a*a + b*b == c*c:
            return "Pythagorean triple"
        return "Not a Pythagorean triple"
    # since n >=2 as per the question, we need not explicitly write elif n > 2
    elif a**n + b**n == c**n:
        return "Fermat was wrong!"
    return "Not a counter-example"


# Tests for fermat_check go here


def sum_divisors(n, d):
    """
    Purpose, Contracts & Requirements go here
    """
    if d == 0:
        return 0
    elif n % d == 0:
        return d + sum_divisors(n, d-1)
    return sum_divisors(n, d-1)


def is_perfect_num(n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return n == sum_divisors(n, n//2)

# Tests for is_perfect_num go here


def sum_divisors_alt(n, d):
    """
    Purpose, Contracts & Requirements go here
    """
    # think about n==6 case to understand the reason of using math.ceil below
    if d > math.ceil(math.sqrt(n)):
        return 0
    elif n % d == 0:
        return d + sum_divisors(n, d+1)
    return sum_divisors(n, d+1)


def is_perfect_num_alt(n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return n == sum_divisors_alt(n, 1)


# Tests for is_perfect_num_alt go here
