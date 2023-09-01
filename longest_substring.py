# With given string S, find the length of the longest substring without repeating any character.

# Example: S: abccabd
# result: 4
# explaination: cabd

def find_longest_substring(s):
    max_possible_len = len(set(s))
    found_chars = {}
    length = 0
    max_length = 0
    current = 0
    while current != len(s):
        # print(current)
        if max_length == max_possible_len:
            return max_length
        if s[current] not in found_chars.keys():
            length += 1
            found_chars[s[current]] = current
            current += 1
            if max_length < length:
                max_length = length
        else:
            current = found_chars[s[current]]+1
            found_chars = {}
            if max_length < length:
                max_length = length
            length = 0
    return max_length


print(find_longest_substring(s='abcabcbb'))
print(find_longest_substring(s='bbbbb'))
print(find_longest_substring(s='pwwkew'))
# print(find_longest_substring(S='abcbadb'))
