
# as the question given, can have multiple output arrays, but must be in increment order


def threeNumberSum(arr, target):
    # creat an empty array to stire triplets result
    triplets = []
    # get the length of the input numbers
    length = len(arr)
    # per question if no such triplets can be found in the array, the function should return an empty array
    if length < 3:
        return triplets

    # sort input numbers, to keep the increasing order
    arr.sort()
    # store all numbers to a set (目的是为了去重吗？不是)
    # The set is used to check whether there is an existing number to avoid O(n) lookup to find target sum.
    num_set = set(arr)
    for i in range(length):
        # assume if its 2sum, so arr[i] plus a temporary target should equal to the target number
        # i is the first element of the triplets
        tmp_target = target - arr[i]

        # j is index for the second element of the triplets, which starts from smallest value after index i
        for j in range(i + 1, length):
            # last is the third element of the triplets
            last = tmp_target - arr[j]
            # check the numbers to see if "last" is exist and has to be increasing order
            if last in num_set and last > arr[j]:
                # if "last" exits we found all 3 numbers
                triplets.append([arr[i], arr[j], last])
        # remove current number and move to next mumber
        num_set.remove(arr[i])

    return triplets


# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.
 # remind me of two sum, so inside two sum adding a for loop to find the third number

# 2.when you were doing the question, what caused an issue, how did you fix it
 # I didn't figure out how to find the third number fast, found it by using the set

# 3.time/space complexity of your solution?
 # time complexity O(n2) because of the nested loop, Time complexity is O(n^2) because of sorting is O(n*log(n)), and the nesting for loop is O(n*n).

 # space complexity: we didn't use extra space except triplets so it is O(1)

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
 # Maybe to use Hash table
