# if文
bool_var = True
print('boolの計算結果: {}'.format(bool(bool_var)))
if bool_var:
    print('if文の中の処理')

var = 12
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行される

var = 0
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行されない

var = ''
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行されない

var = []
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行されない

var = [0, 1]
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行される

class ClassA():

    def __init__(self,a):
        self.a = a

    def __bool__(self):
        if self.a == 'a':
            return True
        return False

var = ClassA('b')
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print('if文の中の処理') # 実行されない
