#  best case = N**2  ||  average case = N**2  ||  worst case = N**2
def merge(arr, l, m, r):        # l =left, m = mid, r = right

    n1 = m - l + 1              # n1 是 索引值0~中間節點的長度
    n2 = r - m                  # n2 是 中間節點~last index的長度
    L = [0]*(n1 + 1)            # 建立左半部的0陣列, 並在最後面加上一格存無限大的空間
    R = [0]*(n2 + 1)            # 建立右半部的0陣列, 並在最後面加上一格存無限大的空間

    for i in range(0, n1):  # 左半部陣列為左節點開始, 存入
        L[i] = arr[l + i]
    for i in range(0, n2):  # 右半部陣列為(m+1)開始, 存入
        R[i] = arr[m + 1 + i]

    L[n1] = float("inf")        # 此數字為無限大的表示方式
    R[n2] = float("inf")
    lid = 0              # 左節點索引值
    rid = 0              # 右節點索引值
    for i in range(l, r + 1):  # 掃描當前切格出來的陣列從左到右, 並進行比較
        if L[lid] <= R[rid]:
            arr[i] = L[lid]     # 比較小的就先行放入到原始陣列
            lid += 1            # 索引值往後移一格
        else:
            arr[i] = R[rid]
            rid += 1


def mergeSort(arr, l, r):
    if l < r:                     # 找到剩餘兩個數字比較, 在recursive回去
        m = (l + (r - 1)) // 2    # 找中間點, 索引值
        mergeSort(arr, l, m)      # 運算切割出來的左半部部分
        mergeSort(arr, m + 1, r)  # 運算切割出來的右半部部分
        merge(arr, l, m, r)
    return arr


array = [9, 1, 10, 4, 2, 3, 7, 6, 8, 5]
print(mergeSort(array, 0, len(array) - 1))