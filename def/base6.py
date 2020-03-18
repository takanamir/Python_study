# サブジェネレータ
def sub_sub_generator():
    yield "Sub Sub の yield"
    return "Sub Sub の return"

def sub_generator():
    yield "sub の yield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "sub の return"

def generator():
    yield "generator の yield"
    res = yield from sub_generator()
    print("gen res = {}".format(res))
    return "generator の return"

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

"""
generator の yield
sub の yield
Sub Sub の yield
sub res = Sub Sub の return
gen res = sub の return
Traceback (most recent call last):
  File "base6.py", line 22, in <module>
    print(next(gen))
StopIteration: generator の return
"""
