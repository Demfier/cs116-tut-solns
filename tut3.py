# This file contains solutions to CS116, Tutorial 3
import math
import check

# CQ1: D)
# CQ2: A)


def closest_integer():
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    input_num = float(input("What's the number?"))
    int_part = int(input_num)
    decimal = input_num - int_part
    if decimal < 0.5:  # see, this wasn't very complicated, was it?
        return int_part - 1
    elif decimal >= 0.5:
        return int_part + 1
    return int_part


# Tests for closest_integer go here


def create_date():
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    # The funny things you could with Python!
    return '{2}/{1}/{0}'.format(input('Enter the year: '),
                                input('Enter the month: '),
                                input('Enter the date: '))


# Tests for create_date go here


def fill_the_string(s, n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    full_copies = n // len(s)
    truncated_part = n % len(s)
    return s*full_copies + s[:truncated_part]


# Tests for fill_the_string go here


def read_and_sum(curr_sum, nums_to_sum):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if nums_to_sum == 0:
        return 'The sum is {}'.format(curr_sum)
    curr_num = int(input('Enter an integer: '))
    return read_and_sum(curr_num+curr_sum, nums_to_sum - 1)


def sum_up():
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    nums_to_sum = int(input('Enter the amount of numbers to sum: '))
    print(read_and_sum(0, nums_to_sum))


# Tests for sum_up go here


def my_string_count(s, c):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if s == '':
        return 0
    if s[0] == c:
        return 1 + my_string_count(s[1:], c)
    return my_string_count(s[1:], c)  # and we have our own of ver. str.count!


# Test for my_string_count go here
