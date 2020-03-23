# 2分探索(ソートされた配列から値を2分探索で探索)
"""
ソートされた配列から値を2分探索で探索する関数を作成します
配列(すべて正の整数)内に存在しなかった場合は-1を返します

def binary_search(arr, target):
# arr: ソートされた配列
# target: 探索したい値
"""

def binary_search(arr, target):
    mid = len(arr) // 2
    left = 0 # 探索の左端
    right = len(arr) - 1 # 探索の右端
    for i in range(len(arr)): # 配列の長さ分を実行すれば十分
        search_idx = (left + right) // 2 # 中間値(探索のインデックス)
        if arr[search_idx] == target:
            return search_idx
        elif arr[search_idx] > target: # 探索値より大きかった場合
            right = search_idx - 1
        elif arr[search_idx] < target: # 探索値より小さかった場合
            left = search_idx + 1
        if left > right:
            return -1

a = [1,2,3,4,5,6]
print(binary_search(a, 3)) # 2

a = [1,2,3,4,5,6,8]
print(binary_search(a, 7)) # -1
