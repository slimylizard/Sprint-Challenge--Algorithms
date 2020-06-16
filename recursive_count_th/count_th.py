'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    find_th = "th"
    if len(word) == 0:
        return 0
    if word[:2] == find_th:
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])
    # TBC
    
    pass
