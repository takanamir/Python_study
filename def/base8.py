# 高階関数

def print_hello():
    print('hello')

def print_goodbye():
    print('goodbye')

var = ['AA', 'BB', print_hello, print_goodbye]
var[2]() # hello
var[3]() # goodbye

def print_world(msg):
    print('{} world'.format(msg))

def print_konnnichiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konnnichiwa

var = print_hello(print_world) # hello world
var() # こんにちは
