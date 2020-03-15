# all, any
if all((True, 10 < 20, 'a' == 'a')):
    print('allの中の処理') # 全てTrueのときだけ実行される

if any((10 < 20, 10 < 5, 'a' == 'b')):
    print('anyの中の処理') # 1つでもTrueがあれば実行される
