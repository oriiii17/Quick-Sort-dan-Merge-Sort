def quicksort(data, start, end):
    if start < end:
        # partisi dan dapatkan posisi pivot
        pivot_index = partition(data, start, end)
        # proses partisi sebelah kiri
        quicksort(data, start, pivot_index-1)
        # proses partisi sebelah kanan
        quicksort(data, pivot_index+1, end)

#Implementasi dari fungsi partition() adalah sebagai berikut:
def partition(data, start, end):
    # ambil salah satu sebagai pivot- (elemen terakhir)
    pivot = data[end]
    left = start
    right = end- 1
    while left <= right:
        while data[left] < pivot:
            left = left + 1
        while data[right] > pivot:
            right = right- 1
        if left <= right:
            data[left], data[right] = data[right], data[left]
            left = left + 1
            right = right- 1
    # tukar posisi data pada index left dan end
    data[left], data[end] = data[end], data[left]
    return left