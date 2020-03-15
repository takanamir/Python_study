# 辞書の関数
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_dict = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}
car.update(tmp_dict) # carにtmp_dictが追加される(既存の項目は上書き)
print(car) # {'brand': 'Toyota', 'model': 'カローラ', 'year': 2015, 'country': 'Japan', 'prefecture': 'Aichi'}
car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car) # {'brand': 'Toyota', 'model': 'カローラ', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi', 'city': 'Toyota-shi'}

value = car.popitem()
print(car) # {'brand': 'Toyota', 'model': 'カローラ', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi'}
print(value) # ('city', 'Toyota-shi')

value = car.pop('model')
print(car) # {'brand': 'Toyota', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi'}
print(value) # カローラ

car.clear()
print(car) # {}
del car # 変数そのものがなくなる
