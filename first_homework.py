# a = input('переменная 1 ')
# b = input('переменная 2 ')

# print('переменная 1 =', a)
# print('переменная 2 =', b)

# seconds = int(input('количество секунд = ',))
# q = seconds // 3600
# w = (seconds // 60) // 24
# e = seconds % 60
# print(f'время = { q } : { w } : { e } ')

# p = int(input('число до 10 '))
# pp = int( p * 10 + p)
# ppp = int(( p * 100 ) + ( p * 10 ) + p)
# print (int( p + pp + ppp))

# proceed = int(input('выручка '))
# costs = int(input('издержки '))
# j = (proceed-costs)/proceed
# if proceed >= costs:
#     print('профицит, рентабельность выручки - ', "%.5f" % j)
#     if proceed >= costs:
#      sotr = int(input('количество сотрудников '))
#      l = proceed / sotr
#     print('прибыль на 1 сотрудника', "%.3f" % l)
# else:
#     print('убытки')

km = int(input('километры '))
point = int(input('цель '))

while True:
    print("%.3f" % km)
    km += ( km * 0.1 )
    if km >= point:
      break
