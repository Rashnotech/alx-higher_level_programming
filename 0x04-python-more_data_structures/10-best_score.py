#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = max(a_dictionary.items(), key=a_dictionary.get)
        return best
    else:
        return None
