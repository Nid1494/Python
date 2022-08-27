# code
def numberofpainter(arr, maxlength):
    total = 0
    numberpainters = 1
    for i in arr:
        total += i
        if total > maxlength:
            total = i
            numberpainters += 1
    return numberpainters


def partition(arr, j):
    lb = max(arr)
    hb = sum(arr)
    while lb < hb:
        mid = lb + (hb - lb) // 2
        requiredpainters = numberofpainter(arr, mid)
        if requiredpainters <= j:
            hb = mid
        else:
            lb = mid + 1
    return lb


array = [10, 20, 30, 40]
n = len(array)
k = 2
print(int(partition(array, k)))
