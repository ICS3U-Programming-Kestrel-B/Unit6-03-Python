#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 15, 2022
# This program generates 10
# random numbers from 1 to
# 100 and calculates the
# smallest number

import math
import random


def min_value(random_num_list):
    # initializing min_num
    min_num = 100
    counter = 0
    for a_single_number in random_num_list:
        # initializing current_num
        current_num = random_num_list[counter]
        # reassigning min_num
        if min_num > current_num:
            min_num = current_num
        # incrementing counter
        counter = counter + 1
        # deciding whether to end loop
        if counter == 10:
            break
    # returning min_num
    return min_num


def main():
    # introductory paragraph
    print("This program generates 10")
    print("random numbers from 1 to")
    print("100 and calculates the")
    print("smallest number")
    print("")

    # initializing variables
    random_num_list = []

    # generating numbers
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        random_num_list.append(random_num)
        # displaying generated number
        print("{} has been generated.".format(random_num))

    # calling function
    true_min = min_value(random_num_list)

    # displaying results
    print("The lowest number is {}.".format(true_min))


if __name__ == "__main__":
    main()
