# Fibonacci Sequence
# the fiboancci sequence is defined recursively
# every recursion must have a base case like a stopping point, in this case the base case or the exeption is when there are only 2 or less numbers, so when n equals 0,1,2
# f0= 0 f1=0 f2=0,1 fn=fn-1 + fn-2
# Question n intergers so n is not start with 0, also 1<=n<=10


def Fibonacci(n):
    # base(special) case
    # Check if the provided input value, n, is equal to 0, 1 or 2. If true, return N.
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    # recursive(general) case
    # Otherwise, the function fib(int N) calls itself, with the result of the 2 previous numbers being added to each other, passed in as the argument. This is derived directly from the recurrence relation: F_{n} = F_{n-1} + F_{n-2}
    else:
        # results
        # Do this until all numbers have been computed, then return the resulting answer.
        res = Fibonacci(n-1)
        res.append(res[-2]+res[-1])
        return res

# 我有点混乱用recursion和只用iteration的区别和怎么分辨

# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.
   # The fiboancci sequence is defined recursively, so we can use recursion to compute fibonancci sequence. At first, with the constrain of N given, find the base case and recursive case.

# 2.when you were doing the question, what caused an issue, how did you fix it
  # I didn't recognize the question asked to return array first

# 3.time/space complexity of your solution?
  # Time complexity  O(n): The only uncertain one is the line: res = Fibonacci(n-1). Since it's a recursive call, the total time complexity should be O(1) + O(Fibonacci(n - 1). And we can analyze the O(Fibonacci(n - 1).
    # O(Fibonacci(n - 1) = O(1) + O(Fibonacci(n - 2), till n == 2. Since there is n - 2 times function call to Fibonacci. It would be O((n - 2) * 1) = O(n).
  # Space complexity : O(N) We need space proportionate to N to account for the max size of the stack, in memory. This stack keeps track of the function calls to fib(N). This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a StackOverflowError.

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
 # Since the input n has an upper limit and the nature of the Fibonacci numbers: the index for each number is certain. We can pre-calculate an array store in disk or memory. Every time get a call just return the sliced array like: RES_ARRAY[:n]


# Improve upon the recursive option by using iteration, still solving for all of the sub-problems and returning the answer for N, using already computed Fibonacci values. In using a bottom-up approach, we can iteratively compute and store the values, only returning once we reach the result.
# If N is less than or equal to 1, return...
# Otherwise, iterate through N, storing each computed answer in an array along the way.
# Use this array as a reference to the 2 previous numbers to calculate the current Fibonacci number.
# Once we've reached the last number, return it's Fibonacci number.
