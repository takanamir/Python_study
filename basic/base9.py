# リスト(最初に大きさを宣言する必要がない)
# list_a = [1,2,3,4]
# list_b = [] # 空のリスト
#
# print(list_a)
# print(list_a[0]) # 1
# print(list_a[1]) # 2
#
# list_a = [1,[1,2,'apple'],3,'banana']
#
# print(list_a[1][2]) # apple
# print(list_a) # [1, [1, 2, 'apple'], 3, 'banana']
#
# list_a[1][2] = 'lemon'
# print(list_a) # [1, [1, 2, 'lemon'], 3, 'banana']

# リスト関数
list_a = [1,2,3,4,5]
print(list_a[0:2]) # [1, 2]
print(list_a[2:]) # [3, 4, 5]
print(list_a[:3]) # [1, 2, 3]

list_b = list_a[:3]
print(list_b) # [1, 2, 3]
print(list_a[0:5:2]) # [1, 3, 5] ← 1つ飛ばし

# append(追加。リストを追加すると多重配列化する), extend(リストをそのまま追加して拡張)
list_a.append('apple')
print(list_a) # [1, 2, 3, 4, 5, 'apple']
list_a.extend(['banana', 'lemon'])
print(list_a) # [1, 2, 3, 4, 5, 'apple', 'banana', 'lemon']
list_a.insert(1, 'grape')
print(list_a) # [1, 'grape', 2, 3, 4, 5, 'apple', 'banana', 'lemon']
# list_a.clear()
# print(list_a) # []

# remove, pop, count
list_a.remove(3)
print(list_a) # [1, 'grape', 2, 4, 5, 'apple', 'banana', 'lemon']
value = list_a.pop(1)
print(list_a) # [1, 2, 4, 5, 'apple', 'banana', 'lemon']
print(value) # grape
print(list_a.count('banana')) # 1
print(list_a.index('apple')) # 4

# copy
# list_b = list_a # 参照先が一致
# print(list_a)
# list_b[0] = 'AAAAA'
# print(list_a) # ['AAAAA', 2, 4, 5, 'apple', 'banana', 'lemon']

list_b = list_a.copy()
print(list_a)
list_b[0] = 'AAAAA'
print(list_a) # [1, 2, 4, 5, 'apple', 'banana', 'lemon']
print(list_b) # ['AAAAA', 2, 4, 5, 'apple', 'banana', 'lemon']

# sort, reverse
list_a = [1,7,9,4,0,6]
print(list_a)
list_a.sort() # 同じ型でないとできない
print(list_a) # [0, 1, 4, 6, 7, 9] ← 昇順
list_a.reverse()
print(list_a) # [9, 7, 6, 4, 1, 0] ← 降順。直前のsort()がないと、[6, 0, 4, 9, 7, 1]になる

list_a = ['banana', 'lemon', 'apple', 'grape']
print(list_a)
list_a = sorted(list_a) # = で繋いで値を入れる必要あり
list_a.reverse()
print(list_a) # ['lemon', 'grape', 'banana', 'apple']
