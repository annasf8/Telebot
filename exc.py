import statistics

def find_median(arr):
    arr = sorted(arr)
    print(arr)
    for i in arr:
        if i in arr:
            i = statistics.median(arr)
            return i
        else: return None
print(find_median([1, 5, 2, 3, 6]))
print(find_median([100, 5, 2, 4, 3, 6]))
print(find_median([]))
