# タプル(値を変更・追加できないが、アクセス速い、ハッシュ化して利用できる、値が変更されない保証ある)
fruit = ('apple', 'banana', 'lemon')

print(fruit)
print(type(fruit)) # <class 'tuple'>
print(fruit[0])

# fruit[1] = 'grape' # エラー
fruit = fruit + ('grape',)
print(fruit) # ('apple', 'banana', 'lemon', 'grape')

list_fruit = ['apple', 'banana']

fruit = tuple(list_fruit)
print(fruit) # ('apple', 'banana')
print(fruit.count('apple')) # 1
print(fruit.index('apple')) # 0

pos = (135,35)

countries = {pos: 'Japan'}

print(countries.get((135,35))) # Japan
