# Dictionary(辞書型)
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

print(car['brand']) # 存在しなければエラー
print(car.get('bran')) # 存在しなければNone
print(car.get('bran', 'Does not exist')) # Does not exist
print(car.get('bran', 12)) # 12

print(car.get(1)) # 100

print(car.keys()) # dict_keys(['brand', 'model', 'year', 1]) ← キー一覧
print(car.values()) # dict_values(['Toyota', 'Prius', 2015, 100]) ← 値一覧
print(car.items()) # dict_items([('brand', 'Toyota'), ('model', 'Prius'), ('year', 2015), (1, 100)]) ← キー + 値

for k, v in car.items():
    print('key = {}, value = {}'.format(k, v))

if 'brand' in car:
    print('carのブランドは{}'.format(car['brand'])) # carのブランドはToyota
