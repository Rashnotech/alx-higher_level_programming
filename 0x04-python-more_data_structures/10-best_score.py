#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = max(a_dictionary.items())
        return best[0]
    else:
        return None
