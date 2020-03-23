# リスト内包表記

list_a = (1,2,3,'a',4,'b') # タプル

list_b = [x*2 for x in list_a] # list_a のリスト
print(list_b) # [2, 4, 6, 'aa', 8, 'bb']

list_b = [x*2 for x in list_a if type(x) == int] # list_a のリスト
print(list_b) # [2, 4, 6, 8]

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c) # [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c) # ['Apple', 'Banana']

list_a = (x for x in range(100))
print(type(list_a)) # <class 'generator'>

list_a = tuple(x for x in range(100))
print(type(list_a)) # <class 'tuple'>

def func(n):
    for x in range(2, n):
        if n % x == 0:
            return False

list_a = [x for x in range(100) if func(x) == False]
print(list_a)
"""
[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30,
32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 5
5, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78
, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]
"""
