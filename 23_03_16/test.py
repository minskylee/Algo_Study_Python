arr = [1, 2, 3, 3, 3, 5, 6, 7]
M = 3
s, e = 0, len(arr) - 1
while s != e:
    mid = (s + e) >> 1
    if arr[mid] >= M:
        e = mid
    else:
        s = mid + 1
a = s
s, e = 0, len(arr) - 1
while s <= e:
    mid = (s + e) >> 1 
    if arr[mid] > M:
        e = mid - 1
    else:
        s = mid + 1
b = s
print(a, b, b - a)
print(arr)
