
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
