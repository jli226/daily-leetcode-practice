def balancedBrackets(string):
    brackets_map = {"[": "]", "(": ")", "{": "}", "|": "|"}
    open_bra = set(["[", "(", "{", "|"])
    brackets = set(["[", "]", "(", ")", "{", "}", "|"])
    stack = []

    for i in string:
        if i not in brackets:
            continue
        if i in open_bra:
            if i == "|":
                if stack and stack[-1] == "|":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        elif stack and i == brackets_map[stack[-1]]:
            stack.pop()
        else:
            return False
