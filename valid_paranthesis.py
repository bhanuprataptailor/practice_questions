def check_if_valid_paranthesis(str):
    stack = []
    paranthesis_map = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    open_paranthesis = ["(", "[", "{"]

    for p in str:
        if p in open_paranthesis:
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != paranthesis_map[p]:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


print(check_if_valid_paranthesis(str='{[]}'))
print(check_if_valid_paranthesis(str='{]'))
print(check_if_valid_paranthesis(str='{{'))
print(check_if_valid_paranthesis(str=''))
print(check_if_valid_paranthesis(str='[{}()]'))
