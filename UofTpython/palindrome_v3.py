def is_palindrome_v3(s):
    """ (str) -> bool

    Return True if and only if x is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """
    # var beginning of string
    i = 0
    # var end of string
    j = len(s)-1

    # Loop iterates as long as the letters in each half match until all letters are checked.
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If the loop completed with J <= i, then the word must be a palindrome.
    return j <= i

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''

    # For each character in s, add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev
