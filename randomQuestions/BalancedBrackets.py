def balancedBrackets(string):
    # store all possible open and close brackets as key and value in a dictionary
    brackets_map = {"[": "]", "(": ")", "{": "}", "|": "|"}
    # created a set with only open bracket
    open_bra = set(["[", "(", "{", "|"])
    # created a set with all brackets
    brackets = set(["[", "]", "(", ")", "{", "}", "|"])
    # initialize an empty stack to keep track of opening brackets
    stack = []

    # process each bracket of the string one at a time
    for i in string:
        # If the character is not in the set of all brackets, we ignore it.
        if i not in brackets:
            continue
        # if we encounter an opening braket, we simply push it onto the stack and process it later
        if i in open_bra:
            # a special case "|"'s opening and closing brackets are the same, when we encounter an "|", check the stack
            if i == "|":
                # if there is at least one element in the stack and the last element in the stack is "|", we pop the last element
                if stack and stack[-1] == "|":
                    stack.pop()
                # if not, we add "|" to the stack
                else:
                    stack.append(i)
            # any other opening bracket we encounter, it should be added to the stack
            else:
                stack.append(i)
        # if we encoiunter a closing bracket then we check the element on the top(last) of the stack. If the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing. Else, this implies an invalid expression.

        elif stack and i == brackets_map[stack[-1]]:
            stack.pop()
        # in the end, if we are left with a stack still having elements, then this implies an not balanced brackets
        else:
            return False


# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.
  # The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards. As above line by line explaination.

# 2.when you were doing the question, what caused an issue, how did you fix it
  # I didn't consider "|" special case at first, because it has same open and close brackets. I fixed it by adding a if/else just for "|" situation

# 3.time/space complexity of your solution?
 # Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
 # Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
# Move all the brackets, open_bra, and brackets_map out of the function. Make them constants to save space.

  # Hash map for keeping track of mappings. This keeps the code very clean.
  # Also makes adding more types of parenthesis easier
  # not sure what else can improve
