# This file contains solutions to CS116, Tutorial 1
import math
import check

# CQ1: B) 25.0 (in python3, / returns a float by default)


def create_acct_num(n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10

    # Does there exist a generalized formula to retrive
    # the ith digit in a positive integer?
    last_digit = (ones + tens + hundreds) % 7
    return (n*10 + last_digit)


# Tests for create_acct_num go here


def shipping_charges(handling, charge_per_kg, weight_per_box, num_boxes):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    before_taxes = (num_boxes * weight_per_box * charge_per_kg) + handling
    tax = 0.13
    return before_taxes * (1+tax)


# Tests for shipping_charges go here


def std_dev(x1, x2, x3, x4, x5):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    x_mean = (x1 + x2 + x3 + x4 + x5) / 5
    expr = ((x1 - x_mean)**2) + ((x2 - x_mean)**2) + ((x3 - x_mean) ** 2) + \
        ((x4 - x_mean)**2) + ((x5 - x_mean)**2)
    return math.sqrt(expr)


# Tests for std_dev go here


def cell_charge(minutes, data):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    free_mins = 200
    charge_per_min = 0.5  # after 200 free "anytime" minutes
    free_mb = 100
    charge_per_150mb = 5.00  # per 150 MB after first 100 MB of data
    monthly_charge = 39.00

    call_charge = (minutes - free_mins) * charge_per_min
    data_charge = math.ceil((data - free_mb) / 150) * charge_per_150mb
    return monthly_charge + max(0, call_charge) + max(0, data_charge)


# Tests for cell_charge go here
