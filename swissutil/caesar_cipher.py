def rot15(s):
    """A nordic-friendly version of rot-13 encoding.

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
    chars = u"abcdefghijklnmopqrstuvwxyzåäöø"
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
