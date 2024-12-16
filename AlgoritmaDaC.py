# untuk nilai terkecil/terbesar
import math

def max(data, start, end, max_value):
    # base case
    if start == end:
        max_value = data[start]
        return max_value
    # base case
    elif start == end- 1:
        if data[start] > data[end]:
            max_value = data[start]
            return max_value
        else:
            max_value = data[end]
            return max_value
    else:
        # recursive case
        mid = (start + end) // 2
        # ruas kiri
        left_max = max(data, start, mid, max_value)
        # ruas kanan
        right_max = max(data, mid+1, end, max_value)
        # combine
        if left_max > right_max:
            return left_max
        else:
            return right_max
# bagian utama program, untuk mencoba
data = list([150, 24, 13, 12, 1, 10, 140, 11])
print(max(data, 0, len(data)-1,-math.inf))