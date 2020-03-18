# inner関数、ノンローカル変数

def outer_1():
    outer_value = '外側の関数'
    def inner_1():
        outer_value = '内側の関数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner_1()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer_1()

"""
inner: outer_value = 内側の関数, id = 1191463301456
outer: outer_value = 外側の関数, id = 1191463301360
"""

def outer_2():
    outer_value = '外側の関数'
    def inner_2():
        nonlocal outer_value
        outer_value = '内側の関数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner_2()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer_2()

"""
inner: outer_value = 内側の関数, id = 1913196523856
outer: outer_value = 内側の関数, id = 1913196523856
"""
