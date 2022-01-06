import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Password generator')
number_of_letters = int(input('Number of letters: '))
number_of_numbers = int(input('Number on numbers: '))
number_of_symbols = int(input('Number of symbols: '))
password = ''
pass_len = number_of_letters + number_of_numbers + number_of_symbols
list_for_choice = [letters, numbers, symbols]
while len(password) < pass_len:
    if number_of_symbols == 0:
        list_for_choice.remove(symbols)
        number_of_symbols -= 1
    elif number_of_numbers == 0:
        list_for_choice.remove(numbers)
        number_of_numbers -= 1
    elif number_of_letters == 0:
        list_for_choice.remove(letters)
        number_of_letters -= 1
    random_choise = random.choice(list_for_choice)
    if random_choise == letters:
        number_of_letters -= 1
    elif random_choise == symbols:
        number_of_symbols -= 1
    elif random_choise == numbers:
        number_of_numbers -= 1
    password += random.choice(random_choise)

print(password)
