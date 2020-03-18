# ジェネレータ関数(メモリ使用量を削減できる。DBから大量のデータを取得する時に役立つ)

# def generator(max):
#     print('ジェネレータ作成')
#     for n in range(max): # n:0～9
#         yield n
#         print('yield実行')

def generator(max):
    print('ジェネレータ作成')
    for n in range(max): # n:0～9
        try:
            x = yield n
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')

gen = generator(10)
next(gen) # xはNone
gen.send(100) # xは100
gen.close() # StopIterationする
next(gen)
# gen.throw(ValueError('Invalid Value'))
# n = next(gen) # ジェネレータ作成
# print('n = {}'.format(n)) # n = 0
# n = next(gen) # yield実行
# print('n = {}'.format(n)) # n = 1

# for x in gen:
#     print('x = {}'.format(x))
"""
x = 0
yield実行
x = 1
yield実行
x = 2
yield実行
x = 3
yield実行
x = 4
yield実行
x = 5
yield実行
x = 6
yield実行
x = 7
yield実行
x = 8
yield実行
x = 9
yield実行
"""
