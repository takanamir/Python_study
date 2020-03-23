# マージソート(列を分割し、1まで分割したら併合しながら整列させる)
"""
以下のリストをマージソートを用いて昇順に並び替える
list_a = [5,7,4,5,1,2,3,2,9,1,4]
"""

def merge_sort(arr):
    if len(arr) > 1:
        res = [] # 返り値の配列
        mid = len(arr) // 2 # 配列の真ん中の値
        L = arr[:mid] # [1,2,3,4] => [1,2]
        R = arr[mid:] # [1,2,3,4] => [3,4]
        L = merge_sort(L) # [3,1] => [1,3]
        R = merge_sort(R) # [2] => 2
        i = j = 0 # iはLを探索するインデックス、jはRを探索するインデックス

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            elif L[i] > R[j]:
                res.append(R[j])
                j += 1
            else:
                res.append(L[i])
                i += 1
        while i < len(L):
            res.append(L[i])
            i += 1
        while j < len(R):
            res.append(R[j])
            j += 1
        return res
    else:
        return arr

list_a = [5,7,4,5,1,2,3,2,9,1,4]
print(merge_sort(list_a))
