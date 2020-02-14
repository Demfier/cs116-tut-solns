# This file contains solutions to CS116, Tutorial 5
import math
import check

# CQ2: B) NO
# CQ3: A) YES


def record_digits_acc(n, pos, acc):
    """
    Purpose, Contracts & Requirements go here
    """
    if pos == len(n):
        return acc
    acc[int(n[pos])] += 1
    return record_digits_acc(n, pos+1, acc)


def record_digits(n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return record_digits_acc(str(n), 0, [0]*10)


# Tests for record_digits go here


def count_max_acc(alon, curr_max, count, pos):
    """
    Purpose, Contracts & Requirements go here
    """
    if pos == len(alon):
        return count
    curr_num = alon[pos]
    if curr_num > curr_max:
        curr_max = curr_num
        count = 0
    if curr_num == curr_max:
        count += 1
    return count_max_acc(alon, curr_max, count, pos+1)


def count_max(alon):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return count_max_acc(alon, alon[0], 0, 0)


# Tests for count_max go here


def smaller(s):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if len(s) == 1:
        return s
    if s[0] > s[-1]:
        return smaller(s[1:])
    return smaller(s[:-1])


# Tests for smaller go here


def skip_value(L):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if L == []:
        return 0
    step_size = L[0]
    if step_size > len(L):
        return 1
    return 1 + skip_value(L[step_size:])


# Tests fro skip_value


def list_to_num_acc(digits, num, pos):
    """
    Purpose, Contracts & Requirements go here
    """
    if digits == []:
        return num
    num += digits[-1] * (10 ** (pos))
    return list_to_num_acc(digits[:-1], num, pos+1)


def list_to_num(digits):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return list_to_num_acc(digits, 0, 0)
