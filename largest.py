#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that finds the largest of 10 numbers

import random


def number_list(array):

    large_number = 0
    for counter in range(0, len(array)):
        top = array[counter]
        if large_number < top:
            large_number = top

    return large_number


def main():
    # This is the main function

    random_numbers = []
    largest_number = 0

    # Input
    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        random_numbers.append(random_number)
        print("The Random Number is: {0}".format(random_number))
    print("")

    largest_number = number_list(random_numbers)

    print("The highest number is: {0} ".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
