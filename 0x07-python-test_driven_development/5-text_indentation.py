#!/usr/bin/python3
"""

this module is a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    t = text[:]

    for e in ".?:":
        list_text = t.split(e)
        t = ""
        for m in list_text:
            m = m.strip(" ")
            t = m + e if t is "" else t + "\n\n" + m + e

    print(t[:-3], end="")
