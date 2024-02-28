"""
Starter code for Advent of Code 2019 Day #1

You must implement functions part1 and part2
"""

import sys
import os


def part1(numbers):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """
    total = 0
    for val in numbers:
        total += val // 3 - 2
    return total


def part2(numbers):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - numbers (list of integers)

    Returns an integer
    """

    ### Replace with your code
    return None


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################