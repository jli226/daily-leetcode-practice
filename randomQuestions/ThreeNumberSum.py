
def threeNumberSum(arr, target):
    triplets = []
    length = len(arr)
    if length < 3:
        return triplets

    arr.sort()
    num_set = set(arr)
    for i in range(length):
        tmp_target = target - arr[i]
        for j in range(i+1, length):
            last = tmp_target - arr[j]
            if last in num_set and last > arr[j]:
                triplets.append([arr[i], arr[j], last])
        num_set.remove(arr[i])

    return triplets


# 1.talk through your code in a high level,how you solved it at a conceptual level, dodn't just read your code line by line.

# 2.when you were doing the question, what caused an issue, how did you fix it

# 3.time/space complexity of your solution?

# 4.What are some ways in which we could tweak / change my implementation to improve on its better time / space complexity?
