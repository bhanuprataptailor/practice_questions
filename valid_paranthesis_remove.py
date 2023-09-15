def check_valid_str_remove(str):
    stack = []
    paranthesis_map = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    open_paranthesis = ["(", "[", "{"]
    moves = 0
    for p in str:
        if p in open_paranthesis:
            stack.append(p)
        else:
            if len(stack) == 0:
                moves += 1
            else:
                if stack[-1] != paranthesis_map[p]:
                    moves += 1
                else:
                    stack.pop()

    moves += len(stack)
    return moves


print(check_valid_str_remove(str='{[]}'))
print(check_valid_str_remove(str='{]'))
print(check_valid_str_remove(str='{{'))
print(check_valid_str_remove(str=''))
print(check_valid_str_remove(str='[{}()]'))
print(check_valid_str_remove(str='}}(('))
print(check_valid_str_remove(str='}(())}'))
