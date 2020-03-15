# セットの関数
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s | t # 和集合
u = s.union(t) # 和集合
print(u)

v = s & t # 積集合
print(v)

w = s - t # 差集合
print(w)

x = s ^ t # どちらか一方にだけある要素を返す
x = s.symmetric_difference(t)
print(x)

s |= t # => s = s | t => sがsとtの和集合 => sにtの要素が入る
print(s)

# issubset(子集合か), issuperset(親集合か), isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) # True
print(s.issuperset(t)) # False
print(t.isdisjoint(s)) # False
print(t.isdisjoint(u)) # True
