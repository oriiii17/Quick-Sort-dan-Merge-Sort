def mergesort(data): # data = list
    if len(data) > 1:
        # cari titik tengahnya
        mid = len(data) // 2
        # berdasarkan mid, bagi data menjadi dua bagian
        # pada python bisa menggunakan slicing
        left = data[:mid]
        right = data[mid:]

        # bagi lagi sampai bagian terkecil secara rekursif
        mergesort(left)
        mergesort(right)

        # merge kiri dan kanan sehingga hasilnya terurut
        # i => untuk index potongan kiri, j => untuk index potongan kanan
        i = 0
        j = 0
        # k = untuk index list hasil penggabungan kiri dan kanan
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        # Jika salah satu sudah habis, sisanya tinggal dimasukkan ke list hasil
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k]=right[j]
            j += 1
            k += 1