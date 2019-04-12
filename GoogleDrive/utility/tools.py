"""This module provides some function that helps coding easier.

Function in this module:
    -   get_full_path(file) -> return full path of file.
"""

from os import path


def get_full_path(file):
    """
    get_full_path(file) -> return full path of file.
    This function figures out exactly the path of file on system.
    Required argument:
        file    --  a string-type file name.
    """
    if file[0] == '~':
        file = path.expanduser(file)
    else:
        file = path.realpath(file)
    return file
