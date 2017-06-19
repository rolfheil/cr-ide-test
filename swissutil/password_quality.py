# -*- coding: utf-8 -*-
""" This module i

"""
import sys


ERROR_MESSAGE = "String is rejected!"
SUCCESS_MESSAGE = "String is acceptable"
MIN_PASSWORD_LENGTH = 6

#note the ugly function name, we will refactor that in a minute
def evaluate_password_quality(input_):
    """ Tests that the string is an acceptable password.

        Parameters
        ----------
         input_: str
            the string to be tested

        Returns
        -------
        int
            0 if string was an acceptable password, -1 if it was not
    """
    string_acceptable = is_acceptable(input_)
    #printing messages is typically not desirable behaviour, it will go away
    if string_acceptable:
        return 0
    else:
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
    numbers = has_numbers(input_)
    lower = has_lower(input_)
    upper = any(char.isupper() for char in input_[1:-1])
    has_length = len(input_) > MIN_PASSWORD_LENGTH
    return numbers and lower and upper and has_length

def has_numbers(string_, ignore_chars=1):
    """ Checks a string for numbers.
    
    Parameters
    ----------
    string_: str 
        the string to test against
    ignore_chars: int
        ignore first *and* last n characters
    Returns
    -------
    bool
        whether or not the string contains one or more numbers

    """
    return  any(char.isdigit() for char in string_[ignore_chars:-ignore_chars])

def has_lower(string_, ignore_chars=1):
    """ Check a string for lower case characters.

    Parameters
    ----------
    string_: str
        the string to test against

    Returns
    -------
    bool
        whether or not the string contains one or more lower case characters


    """
    return  any(char.islower() for char in string_[ignore_chars:-ignore_chars])

def has_upper(string_, ignore_chars=1):
    """ Check a string for upper case characters.

      Parameters
      ----------
      string_: str
          the string to test against

      Returns
      -------
      bool
          whether or not the string contains one or more lower case characters


      """
    return any(char.islower() for char in string_[ignore_chars:-ignore_chars])
