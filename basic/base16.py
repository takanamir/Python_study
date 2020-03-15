# if and or not
# msg = 'yellow'
# if msg == 'blue': # 文字列同士も比較できる
#     print('すすめ')
# elif msg == 'red':
#     print('とまれ')
# else:
#     print('それ以外の処理')

age = 30
if age < 20:
    print('20未満')
elif age <= 40: # 20以上40以下
    print('20以上、40以下です')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

# and or not
gender = 'man'
age = 10
if gender == 'man' and age <= 20:
    print('未成年男性です')
if gender == 'man' or age <= 20:
    print('男性もしくは20未満です')

gender = 'woman'
age = 40
if not gender == 'man': # if gender != 'man': でも同じ
    print('男ではない')
