# This file contains solutions to CS116, Tutorial 4
import math
import check

# CQ1: E)


def create_cards(values, suits):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return list(map(lambda x: [x, suits[values.index(x)]], values))


# Tests for create_cards go here


def choose_by_color(loC, color):  # Abs. list impl. (really unoptimized!!)
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if color == 'red':
        lookup_list = ['diamonds', 'hearts']
    else:
        lookup_list = ['spades', 'clubs']
    return list(map(lambda x: x[0], filter(lambda x: x[1] in lookup_list, loC)))


def filter_and_convert(loC, lookup_list, val_list):
    if loC == []:
        return val_list
    if loC[0][1] in lookup_list:
        val_list.append(loC[0][0])
    return filter_and_convert(loC[1:], lookup_list, val_list)


def choose_by_color(loC, color):  # recursive impl.
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if color == 'red':
        lookup_list = ['diamonds', 'hearts']
    elif color == 'black':
        lookup_list = ['spades', 'clubs']
    return filter_and_convert(loC, lookup_list, [])


# Tests for choose_by_color go here


def flip_color(c):  # fancy impl.
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    flip_list_1 = ['hearts', 'spades']
    flip_list_2 = ['diamonds', 'clubs']
    # new_index = len(flip_list) - index of curr suit in flip_list - 1
    if c[1] in flip_list_1:
        new_index = 1-flip_list_1.index(c[1])
        c[1] = flip_list_1[new_index]
    else:
        new_index = 1-flip_list_2.index(c[1])
        c[1] = flip_list_2[new_index]


def flip_color(c):  # bland impl.
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if c[1] == 'spades':
        c[1] = 'hearts'
    elif c[1] == 'hearts':
        c[1] = 'spades'
    elif c[1] == 'diamonds':
        c[1] = 'clubs'
    else:
        c[1] = 'diamonds'


# Tests for flip_color go here


def flip_hand_helper(loC, pos):
    if pos == len(loC) or loC == []:
        return loC
    flip_color(loC[pos])
    return flip_hand_helper(loC, pos+1)


def flip_hand(loC):
    return flip_hand_helper(loC, 0)


# Tests for flip_hand go here

def last_occ_index(list_of_vals, val, pos):
    if pos < 0:
        return -1
    if list_of_vals[pos] == val:
        return pos
    return last_occ_index(list_of_vals, val, pos-1)


def modify_list(nums, n):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    if n not in nums:
        nums.append(n)
    elif nums.count(n) == 1:
        nums.remove(n)
    elif nums.count(n) >= 2:
        nums.remove(n)
        nums.pop(last_occ_index(nums, n, len(nums) - 1))


# Tests for modify_list go here


def sanitize(s):
    """
    Purpose, Contracts & Requirements, and Examples go here
    """
    return ''.join(list(filter(lambda c: c.isalnum(), s)))


# Tests for sanitize go here
