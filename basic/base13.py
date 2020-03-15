# セット(同じ値入れられない、順序保持されない、高速処理可能)
set_a = {'a', 'b', 'c', 'd', 'a', 12}

print(set_a)
print('e' not in set_a) # True

print(12 in set_a) # True
print(len(set_a)) # 5

# add, remove, discard, pop, clear
set_a.add('e')
print(set_a) # 'e'が除かれる

set_a.remove('e') # 存在しないとエラー
print(set_a) # {'a', 'b', 12, 'd', 'c'}

set_a.discard(12)
print(set_a) # 12が除かれる、存在しなくてもとエラーにならない

val = set_a.pop() # set_aから任意の要素を取り出して削除
print(val)
print(set_a)

set_a.clear()
print(set_a) # set()
