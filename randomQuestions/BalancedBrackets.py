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


# talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.

# when you were doing the question, what caused an issue, how did you fix it

# time/space complexity of your solution?

# What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
