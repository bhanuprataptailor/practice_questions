# Check whether given string s is palindrome or not
# ex:
# aba -> True
# a -> True
# abba-> True
# cda-> False

def is_palindrome(s):
    # if spaces are not ignored
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


special_characters = [' ', ',', '.', '#', ':']


def is_palindrome_i(s):
    # if spaces are ignored, case in sensitive
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] not in special_characters and s[right] not in special_characters:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        elif s[left] in special_characters and s[right] not in special_characters:
            left += 1
        elif s[left] not in special_characters and s[right] in special_characters:
            right -= 1
        else:
            left += 1
            right -= 1
    return True


print(is_palindrome(s='aba'))
print(is_palindrome(s='a'))
print(is_palindrome(s='abba'))
print(is_palindrome(s='cda'))
print(is_palindrome(s=''))

print(is_palindrome(s='ab a'))
print(is_palindrome_i(s='ab a'))

print(is_palindrome(s='ab a'))
print(is_palindrome_i(s='A man, a plan, a canal: Panama'))
