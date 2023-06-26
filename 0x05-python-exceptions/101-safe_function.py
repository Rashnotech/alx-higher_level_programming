#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
    except Exception as err:
        sys.stderr.write(f"Exception: {str(err)}\n")
        return None
    return result
