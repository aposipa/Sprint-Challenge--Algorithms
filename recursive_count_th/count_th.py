'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if len(word) < 2:
        return 0
# checks if the exact two letters are == to "th", then checks through the second index to the end.
    if word[:2] == "th":
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:]) + 0

print(count_th("thanks though but this is through."))
