treasure = r'''         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%'''

print(treasure)
print('Найди сокровище')
print('Ты на развилке, куда пойдешь? Право/лево ')
first_choose = input().lower()
if first_choose == 'право':
    print('Все нормально, идем дальше')
    print('Снова на развилке. Право/лево ? ')
    second_choose = input().lower()
    if second_choose == 'лево':
        print('Молодец, ты нашел сокровище')
    else:
        print('Умер от ловушки')
else:
    print('Умер от нападения скелетов')
