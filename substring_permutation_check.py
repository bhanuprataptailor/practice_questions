def check_substring(str1, master):
    """
        :param str1: string to be checked
        :param master: string to checked with
        :return: if str1 is substring of master

        Complexity:
        Time: O(len(master))
        Space: O(1)
    """

    j = 0
    for i, ch in enumerate(master):
        c = str1[j]
        if c == ch:
            j += 1
        else:
            j = 0
        if j == len(str1):
            return True
    return False


def check_permutation(str1, master):
    """
    :param str1: string to be checked
    :param master: string to checked with
    :return: if str1 is permutation of master

    Complexity:
    Time: O(len(master) + len(str1)) ==> O(len of whichever the longest string)
    Space: O(len(unique_chars_master)) ->> keeping char_count_master dict
    """
    char_count_master = {}
    for c in master:
        if c in char_count_master:
            char_count_master[c] += 1
        else:
            char_count_master[c] = 1

    for c in str1:
        if c not in char_count_master:
            return False
        else:
            if char_count_master[c] == 0:
                return False
            else:
                char_count_master[c] += -1
    return True


print(check_substring(str1='abcdee', master='abcdeerertrt23452dbgkmkdfg'))
print(check_permutation(str1='aabcde', master='baddsbcdwwee'))
