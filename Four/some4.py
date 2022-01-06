import random

rock = 'камень'
paper = 'бумага'
scissors = 'ножницы'

rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

dict_of_choices = {
    rock: rock_img,
    paper: paper_img,
    scissors: scissors_img,
}
keys = list(dict_of_choices.keys())
while(True):
    user_choose = input('Камень, ножницы или бумага: ').lower()
    if user_choose == 'камень' or user_choose == 'ножницы' or user_choose == 'бумага':
        random_choose = random.choice(keys)
        if user_choose == 'камень' and random_choose == paper:
            print(f'{dict_of_choices[random_choose]} \n Ты проиграл')
        elif user_choose == 'ножницы' and random_choose == rock:
            print(f'{dict_of_choices[random_choose]} \n Ты проиграл')
        elif user_choose == 'бумага' and random_choose == scissors:
            print(f'{dict_of_choices[random_choose]} \n Ты проиграл')
        elif user_choose == random_choose:
            print(f'{dict_of_choices[random_choose]} \n Ничья')
        else:
            print(f'{dict_of_choices[random_choose]} \n Ты победил')
    else:
        print('Такого выбора нет')
