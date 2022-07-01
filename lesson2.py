#Армия
soldiers = int(input('Сколько соладат: '))
total_rules = int(input('Количество правил в военском уставе: '))
push_ups = 0
for soldier in range(soldiers - 4, 0, -4):
  print('Солдат под номером -', soldier)
  soldier_rules = int(input('Сколько правил в уставе? '))
  if total_rules != soldier_rules:
    print('Упал-отжался!', 10 * soldier, 'отжиманий!')
    push_ups += 10 * soldier
print('Всего отжиманий -', push_ups)
