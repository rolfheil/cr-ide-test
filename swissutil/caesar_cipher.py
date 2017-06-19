# -*- coding: utf-8 -*-

"""This module implements various Caesar ciphers.

The cipher is a simple replacement of each letter with another one precisely N
steps.

It should not be considered secure unless time-traveling to the year 50 B.C. or
earlier. It is suitable for keeping people from accidentally reading
spoilers etc.

The most famous rotating cipher is of course ROT-13. Because there are 26
alphabets in the Latin alphabet ROT-13 cipher uses the same operation to
both encipher and decipher information.

Both the ROT-13 on latin alphabet and the example ROT-15 with the partial
nordic alphabet have the feature that ROT-13(ROT-13(string)) == string,
which is partially useful in testing.
"""

def rot15(s):
    """A nordic characters-friendly version of rot-13 encoding.

        Parameters
        ----------
        s: string
            the string to be converted, converted to lowercase.
            Valid characters are Latin alphabet and åöäø.

        Returns
        -------
        unicode str
            String rot-15 encoded and in lowercase
    """
    chars = u"abcdefghijklmnopqrstuvwxyzåäöø"
    trans = chars[15:]+chars[:15]
    return unicode('').join(_lookup(c, chars, trans) for c in s )


def _lookup(char, original, rotated):
    """ Looks up a char from rotated from the index where it is found in original. Can be used in e.g.
        Cesar-type encryption.

            Parameters
            ----------
            char: str
               expected to contain 1 character found in the string
            original: str
                the original order of the alphabet
            rotated:
                the rotated character list

            Returns
            -------
            str
                the corresponding index in rotated
    """
    #there is a bug here if char is not found in the original
    # (and another one if original is longer than rotated)
    return rotated[original.find(char)]
