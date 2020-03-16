# enumerate, zip, while
fruits = ['grape', 'pine', 'apple']

for index, value in enumerate(fruits):
    print('index = {}'.format(index))
    print('value = {}'.format(value))
"""
index = 0
value = grape
index = 1
value = pine
index = 2
value = apple
"""

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Taro']

for A, B in zip(classA, classB):
    print('classA student: {}'.format(A))
    print('classB student: {}'.format(B))
"""
classA student: Taro
classB student: Katsuo
classA student: Hanako
classB student: Wakame
classA student: Jiro
classB student: Taro
"""

count = 0
while count < 10: # countが10より小さい場合は中の処理を実行
    print(count) # 0から9まで
    count += 1
