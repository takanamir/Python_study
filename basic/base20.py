# continue(ループ内にcontinueがあると処理が一度飛ばされる)
for i in range(10):
    if i == 3:
        continue
    print(i) # 3だけ飛ばされる
else:
    print('ループ処理終了')

# break(breakが実行されるとループの外に処理が出る)
# breakでループを抜けた場合にはelseは実行されない
num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    if num == 7:
        break
    print(num)
    num += 1
"""
0
1
2
3
4
6
"""

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了') # else実行される
"""
0
1
2
3
4
6
7
8
9
whileループ終了
"""
