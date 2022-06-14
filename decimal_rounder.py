#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: May 2022
# This is a decimal rounder

import math


def round_number(user_num, decimal_round):
    # this function rounds the users input

    # process
    round_num = (user_num[0] * (10**decimal_round)) + 0.5
    round_num = int(round_num)
    round_num = round_num / (10**decimal_round)

    user_num[0] = round_num


def main():
    # this function gets the user input
    user_num_list = []

    # input
    num_input = input("Enter your Number!: ")
    rounded_num = input("Enter the amount of decimals! : ")

    try:
        user_num = float(num_input)
        user_num_list.append(user_num)
        decimal_round = int(rounded_num)
        round_number(user_num_list, decimal_round)
        print("\nThe rounded number is {0}.".format(user_num_list[0]))

    except Exception:
        print("\nInvalid Input!")

    print("\nDone.")


if __name__ == "__main__":
    main()
