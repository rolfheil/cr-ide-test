# -*- coding: utf-8 -*-
""" This module i

"""
import sys


ERROR_MESSAGE = "String is rejected!"
SUCCESS_MESSAGE = "String is acceptable"
MIN_PASSWORD_LENGTH = 6

#note the ugly function name, we will refactor that in a minute
def evaluate_string_for_stuff(foobar):
    """ Tests that the string is an acceptable password.

        Parameters
        ----------
         foobar: str
            the string to be tested

        Returns
        -------
        int
            0 if string was an acceptable password, -1 if it was not
    """
    string_acceptable = is_acceptable(foobar)
    #printing messages is typically not desirable behaviour, it will go away
    if string_acceptable:
        print(SUCCESS_MESSAGE)
        return 0
    else:
        print(ERROR_MESSAGE)
        return -1

def is_acceptable(input_):
    """ Tests that the input string has the following qualities:

        1) it contains a number that is not the first or last character
        2) it contains an uppercase character
        3) it contains a lowercase character
        4) is at least MIN_PASSWORD_LENGHT characters long

        Parameters
        ----------
        input_: str
            the string to be tested

        Returns
        -------
        bool
            True if string is acceptable, False if it is not

    """
    has_numbers = any(char.isalnum() for char in input_[1:-1])
    has_lower = any(char.islower() for char in input_[1:-1])
    has_upper = any(char.isupper() for char in input_[1:-1])
    has_length = len(input_) > MIN_PASSWORD_LENGTH
    return has_numbers and has_lower and has_upper and has_length
