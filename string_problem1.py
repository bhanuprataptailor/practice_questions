# Statement: Given two strings S and T, return True if both the strings are equal, '#' will be counted as backspace.

# Test Case 1:
# S = 'BACK'
# T = 'A#BACC#K'
# Output => True
from time import time


def string_comparision(S, T):
    # complexity: time->O(n+k), space->O(n+k) -> n is len(S), k is len(T)
    str1 = ''
    str2 = ''
    for s in S:
        if s != '#':
            str1 += s
        else:
            str1 = str1[:-1]

    for t in T:
        if t != '#':
            str2 += t
        else:
            str2 = str2[:-1]

    if str1 == str2:
        return True
    return False


def optimal_solution(S, T):
    # complexity: time->O(N), space->O(1) -> don't get confuse with the two while loops,
    # the second while loop is just to count the jump value using backspace count '#'
    p1 = len(S) - 1
    p2 = len(T) - 1
    j1 = 0
    j2 = 0

    while p1 >= 0 and p2 >= 0:
        while S[p1] == '#':
            j1 += 1
            p1 -= 1
            if p1 < 0:
                break
        while T[p2] == '#':
            j2 += 1
            p2 -= 1
            if p2 < 0:
                break
        p1 = p1 - j1
        p2 = p2 - j2
        if p1 >= 0 and p2 >= 0:
            # print(p1, p2)
            if S[p1] != T[p2]:
                return False
            j1 = 0
            j2 = 0
            p1 -= 1
            p2 -= 1
        else:
            return True

    return True


S = '#####BACK'
T = '#####A#BACC#K'

# a = time()
# print(string_comparision(S, T))
# print(time() - a)
# a = time()
# print(optimal_solution(S, T))
# print(time() - a)


S = '#####BACK'
T = '#####A#BACCD#K'

a = time()
print(string_comparision(S, T))
print(time() - a)
a = time()
print(optimal_solution(S, T))
print(time() - a)