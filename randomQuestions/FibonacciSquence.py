# Fibonacci Sequence
# the fiboancci sequence is defined recursively
# every recursion must have a base case like a stopping point, in this case the base case or the exeption is when there are only 2 or less numbers, so when n equals 0,1,2
# f0= 0 f1=0 f2=0,1 fn=fn-1 + fn-2
# Question n intergers so n is not start with 0, also 1<=n<=10


def Fibonacci(n):
    # base case
    if n == 1:
        return []
    elif n == 2:
        return [0, 1]
    # recursive case
    else:
        # results
        res = Fibonacci(n-1)
        # add up last two numbers
        res.append(res[-2]+res[-1])
        return res


# talk through your code ina high level

# what caused an issue, how did you fix it

# time/space complexity of your solution?

# What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
