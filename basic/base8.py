# int, float => str 変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num)) # <class 'str'>
float_num = -20.5
str_float = str(float_num)
print(str_float)
print(type(str_float)) # <class 'str'>

# str => int, float
msg = '12'
int_msg = int(msg)
float_mag = float(msg)

print('value {}, type = {}'.format(int_msg, type(int_msg))) # value 12, type = <class 'int'>
print('value {}, type = {}'.format(float_mag, type(float_mag))) # value 12.0, type = <class 'float'>
