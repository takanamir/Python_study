# 文字列型
# fruit = 'apple' # "" でもよい、\' で、' を文字列として出力できる
# print(fruit)
# print(type(fruit))
#
# print(fruit * 10)
#
# new_fruit = fruit + ' banana'
# print(new_fruit)
#
# fruits = """apple
# banana
# grape
# """
# print(fruits)

# fruit = 'banana'
# print(fruit[2]) # n
#
# # encode, decode(bytes[]型の関数) => bytes[]
# byte_fruit = fruit.encode('utf-8')
#
# print(byte_fruit) # b'banana'
# print(type(byte_fruit)) # <class 'bytes'>
#
# str_fruit = byte_fruit.decode('shift-jis')
# print(str_fruit) # banana
# print(type(str_fruit)) # <class 'str'>

# count関数
# msg = 'ABCDEABC'
#
# # print(msg.count('A')) # 2
# print(msg.count('ABCDEF')) # 0
#
# # startswith, endswith
# print(msg.startswith('ABCD')) # True
# print(msg.endswith('FABC')) # False
#
# # strip, rstrip(右端から削除), lstrip(左端から削除)
# # print(msg.strip('A')) # BCDEABC
# # print(msg.strip('AC')) # BCDEAB
# print(msg.strip('ACB')) # DE
# print(msg.rstrip('ACB')) # ABCDE
# print(msg.lstrip('ACB')) # DEABC
#
# # upper, lower, swapcase, replace, capitalize
# msg = 'abcABC'
# msg_u = msg.upper()
# msg_l = msg.lower()
# msg_s = msg.swapcase()
#
# print(msg_u) # ABCABC
# print(msg_l) # abcabc
# print(msg_s) # ABCabc
#
# # msg_r = msg.replace('c', 'E') # abEABC
# # msg_r = msg.replace('c', '') # abABC
# msg_r = msg.replace('cA', 'DE') # abDEBC
# print(msg_r)
#
# msg = 'ABCDEABC'
# msg_r = msg.replace('ABC', 'abc') # abcDEabc
# print(msg_r)
# msg_r = msg.replace('ABC', 'abc', 1) # abcDEABC ← 1回しか変換されない
# print(msg_r)
# msg_r = msg.replace('ABC', 'abc', 2) # abcDEabc ← 2回まで変換する
# print(msg_r)
# msg_r = msg.replace('ABC', 'abc', -1) # abcDEabc ← デフォルトと同じ
# print(msg_r)
#
# msg = 'hELLO world'
# print(msg.capitalize()) # Hello world ← 1文字目が大文字に・残りは小文字に

# 文字列の一部取り出し、format関数、文字列から数値への変換、islower、isupper
msg = 'h '
print(msg.islower()) # True ← 全て小文字ならTrue
print(msg.isupper()) # False ← 全て大文字ならTrue

msg = 'hello, my name is taro'

print(msg[:5]) # hello
print(msg[:8]) # hello, m
print(msg[8:]) # y name is taro
print(msg[8:11]) # y n
print(msg[-4:]) # taro ← 後ろから数えて
print(msg[-7:]) # is taro
print(msg[0:10:2]) # hlo y ← 1つ飛ばし

name = 'Hanako'
msg = 'my name is {}'.format(name) # 'f'my name is {name}' / 'f'my name is {name=}'
print(msg) # my name is Hanako

msg = '12'
int_msg = int(msg) # 数値にできないものだとエラー
print(int_msg) # 12
print(type(int_msg)) # <class 'int'>

msg = '12.21'
float_msg = float(msg)
print(float_msg) # 12.21
print(type(float_msg)) # <class 'float'>

# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC')) # 0 ← 左端から数えて最初に出る所
print(msg.find('BC')) # 1
print(msg.index('BC')) # 1

print(msg.find('BCDEF')) # -1 ← 見つからなかった場合。index()だとエラー
print(msg.rfind('ABC')) # 5 ← 右端から数えて最初に出る所
