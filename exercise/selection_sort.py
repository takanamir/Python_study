"""
以下のリストを選択ソートを用いて昇順に並び替える
※選択ソート(最小値（最大値）を選んで並び替えて整列させる)
list_a = [5,7,4,5,1,2,3,2,9,1,4]
"""

list_a = [5,7,4,5,1,2,3,2,9,1,4]

# i: 0 => list_aの長さ-1までループしたインデックス
for i in range(len(list_a)):
    # min_idx: 1以上のインデックスで最小値の入っているもの
    min_idx = i
    # j: i+1 => list_aの長さ-1
    for j in range(i+1, len(list_a)):
        if list_a[min_idx] > list_a[j]:
            min_idx = j
    list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)
