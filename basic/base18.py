# for
for i in range(10):
    print(i)

# for _ in range(100): # ループさせるだけ
#     print('A')

for i in range(2, 20, 3): # 2から19まで2つ飛ばし
    print(i)

sample = ['John', 'Paul', 'George', 'Ringo'] # タプルもいける
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
}
for h in human:
    print(h, human.get(h))
"""
Name Taro
Age 20
gender Man
"""
