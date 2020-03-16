# raise, 例外自作

class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        # raise ZeroDivisionError('0では割り切れません')
        raise MyException('0では割り切れません')
    else:
        return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e)) # 0では割り切れません <class '__main__.MyException'>
