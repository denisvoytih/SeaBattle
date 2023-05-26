board = list(range(1, 10)) # Инициализация списка, выступающей в роли игровой доски

def print_board(board): # Функция печати доски
    print ("-------------")
    for i in range(3):
        print ("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print ("-------------")

def take_turn(player_token): # Функция осущесвтляющая ход игрока
    t = False # Переменная для выхода из цикла
    while not t: # Цикл для проверки возможности хода
        player_answer = input("Ваш ход " + player_token+": ")
        try: # Конструкция try-except для проверки ввел ли пользователь число
            player_answer = int(player_answer)
        except:
            print ("Ошибка ! Введите число")
            continue
        if player_answer >= 1 and player_answer <= 9: # Проверка на требуемый диапазон чисел
            if (str(board[player_answer - 1]) not in "XO"): # Проверка на свободность ячейки
                board[player_answer - 1] = player_token
                t = True
            else:
                print ("Ячейка занята")
        else:
            print ("Такой ячейки нет")

def check_win(board): # Функция проверки победы
    win_cells = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) # Выигрышные чейки
    for i in win_cells:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main(board): # Основная функция
    counter = 0 # Счетчик ходов
    win = False # Переменная для выхода из цикла
    while not win:
        print_board(board)
        if counter % 2 == 0:
            take_turn("X")
        else:
            take_turn("O")
        counter += 1
        if counter > 4: # Начиная с четвертого хода проверки на победу
            temp = check_win(board)
            if temp:
                print (temp, "Выиграл!")
                win = True
                break
        if counter == 9: # После окончании 9 хода, вывод ничьи
            print ("Ничья!")
            break
    print_board(board)

main(board)