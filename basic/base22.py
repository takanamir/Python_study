# try, except
try:
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass

print('処理が完了しました。1')

try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('Exception', e, type(e)) # Exception 'list' object has no attribute 'method_a' <class 'AttributeError'>

print('処理が完了しました。2')

try:
    b = [10, 20, 30]
    # c = b.method_a()
    # a = b[4]
    # a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('Exception', e, type(e))
else:
    # a = 10 /0 # この後実行されない
    print('Else処理')

print('処理が完了しました。3')

try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('Exception', e, type(e))
else:
    print('Else処理')
finally: # 成功しても例外発生しても実行される
    print('Finally処理')

print('処理が完了しました。4')
