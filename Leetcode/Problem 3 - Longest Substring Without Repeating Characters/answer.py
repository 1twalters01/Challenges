#  Use a set for uniques if you want it to be faster
def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    start = 0
    end = 0
    max_length = 0
    max_list = []
    uniques = []

    while end < len(s):
        if s[end] not in uniques:
            uniques.append(s[end])
            if len(uniques) > max_length:
                max_length = len(uniques)
                max_list = uniques[::1]
                print(max_list)
            end += 1
        else:
            uniques.remove(s[end])
            start += 1
    return max_length, max_list

s = "abcabcbb"
print(lengthOfLongestSubstring(s))