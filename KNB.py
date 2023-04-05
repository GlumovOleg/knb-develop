# Камень-ножницы-бумага (вариант игрок против игрока и игрок против бота)

import random
from time import sleep
import os
clear = lambda: os.system('cls')
clear()

# Игрок против бота

list = 'камень', 'ножницы', 'бумага'
p = int(input('Введите количество попыток: '))
i = 1
count_player = 0
count_bot = 0
count_none = 0
data = []

while i <= p:
    s = 0
    slovo = input(f'Введите один из вариантов {list}: ')
    player = slovo.lower()
    
    if slovo not in list:
        print('Не верный вариант')
        break

    bot = ''
    data.append(player)
    # print(data)


    print(f'Игрок: {player}')

    if i >= 2:
        print('Бот подключает режим бога...:DDD')
        sleep(1)
        for j in data:
            if data[-2] == 'камень':
                bot = 'бумага'
                print(f'Бот: {bot}')
            elif data[-2] == 'ножницы':
                bot = 'камень'
                print(f'Бот: {bot}')
            elif data[-2] == 'бумага':
                bot = 'ножницы'
                print(f'Бот: {bot}')
            break
    else:
        bot = random.choice(list).lower()
        print(f'Бот: {bot}')

    if (player == 'ножницы' and bot == 'камень') or \
        (player == 'бумага' and bot == 'ножницы') or \
            (player == 'камень' and bot == 'бумага'):
        print('\nИгрок проиграл')
        count_bot += 1

    elif player == bot:
        print('\nНичья')
        count_none += 1

    else:
        print('\nИгрок победил')
        count_player += 1

    def result():
        print(f'Побед игрока: {count_player}')
        print(f'Побед бота: {count_bot}')
        print(f'Сыграно в ничью: {count_none}')
        if count_player == count_bot:
            print('Победа была так близка...')
        elif count_player > count_bot:
            print('Игрок победил!!!')
        elif count_player < count_bot:
            print('Увы и ах... машины скоро нас пороботят...')

    if i == p:
        print(f'\nПопытки исчерпаны {i} из {p}\n')
        result()
        break

    play_again = str(input('\nПродолжить? (да/нет): '))

    if play_again != 'да':
        print(f'\nПройдено {i} попыток из {p}\n')
        result()
        break
    if play_again == 'да':
        clear = lambda: os.system('cls')
        clear()
        i += 1

exit()

# Игрок против игрока

list = ("Камень", "Ножницы", "Бумага")
slovo = input(f'Первый игрок - введите один из вариантов {list}: ')
slovo2 = input(f'Второй игрок - введите один из вариантов {list}: ')

player = slovo
print(f'Первый игрок: {player}\n')
player2 = slovo2
print(f'Второй игрок: {player2}\n')

if (player == 'Ножницы' and player2 == 'Камень') or \
    (player == 'Бумага' and player2 == 'Ножницы') or \
        (player == 'Камень' and player2 == 'Бумага'):
    print('Победил второй игрок')

elif player == player2:
    print('Ничья')
else:
    print('Победил первый игрок')
