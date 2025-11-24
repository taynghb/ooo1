import random
import os#работа с файлами на пк
import json#читать и сохранять результаты в спец формате

def create_board(size, board=False):#поле
    if board == False:
        board = [[' '] * size for _ in range(size)]
    print("\n __" + "____".join(map(str, range(size))))
    for i in range(size):
        print(f"{i}" + "___|".join(board[i]) + "___")
    return board

def check_win(board, player):#проверка выигрыша
    size = len(board)
    for i in range(size):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(size)) or \
            all(board[i][i] == player for i in range(size)) or \
       all(board[i][size-1-i] == player for i in range(size)):
            return True
    return False

def is_board_full(board):#проверка назаполненное поле
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def get_empty_cells(board):#какие клетки пустые
    result = []
    for i in range(len(board)):     
        for j in range(len(board)):      
            if board[i][j] == ' ':    
                result.append((i, j))    
    return result

def robot_move(board, robot_symbol):#ход робота
    empty_cells = get_empty_cells(board)
    player_symbol = 'O' if robot_symbol == 'X' else 'X'
    return random.choice(empty_cells)

def save_stats(winner):
    with open("stats.txt", "a") as f:
        f.write(winner + "\n")

def show_stats():
    try:
        with open("stats.txt", "r") as f:
            games = f.readlines()
        
        x_wins = games.count("X\n")
        o_wins = games.count("O\n")
        draws = games.count("Draw\n")
        total = len(games)
        
        print(f"\nGames: {total} | X: {x_wins} | O: {o_wins} | Draws: {draws}")
    except:
        print("\nNo stats yet")
    
    with open('game_stats/results.json', 'r', encoding='utf-8') as file:
        results = json.load(file)
    
    total = len(results)
    x_wins = sum(1 for game in results if game['winner'] == 'X')
    o_wins = sum(1 for game in results if game['winner'] == 'O')
    draws = sum(1 for game in results if game['winner'] == 'Draw')
    vs_friend = sum(1 for game in results if game['mode'] == 'friend')
    vs_robot = sum(1 for game in results if game['mode'] == 'robot')
    print(f"\n СТАТИСТИКА:")
    print(f"Всего игр: {total}")
    print(f"Побед X: {x_wins}")
    print(f"Побед O: {o_wins}")
    print(f"Ничьих: {draws}")
    print(f"Игр с другом: {vs_friend}")
    print(f"Игр с роботом: {vs_robot}")

def play_with_friend(size, first_player):
    board = create_board(size)
    current_player = first_player
    game_over = False
    winner = "Draw"
    
    while not game_over:
        print(f"\nХодит игрок {current_player}")
        try:
            row = int(input("Строка: "))
            col = int(input("Столбец: "))
            # Проверяем координаты
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Неверные координаты!")
                continue
            # Проверяем, свободна ли клетка
            if board[row][col] != ' ':
                print("Клетка занята!")
                continue
            # Делаем ход
            board[row][col] = current_player
            create_board(size, board)
            
            if check_win(board, current_player):
                print(f" Победил {current_player}!")
                winner = current_player
                game_over = True
            elif is_board_full(board):
                print(" Ничья!")
                game_over = True
            else:
                # Меняем игрока
                current_player = 'O' if current_player == 'X' else 'X'
                
        except ValueError:
            print("Вводите только числа!")
    
    return winner

def play_with_robot(size, first_player):
    board = create_board(size)
    current_player = first_player
    game_over = False
    winner = "Draw"
    
    human_symbol = first_player
    robot_symbol = 'O' if first_player == 'X' else 'X'
    
    while not game_over:
        if current_player == human_symbol:
            # Ход человека
            print(f"\nВаш ход ({human_symbol})")
            try:
                row = int(input("Строка: "))
                col = int(input("Столбец: "))
                
                if row < 0 or row >= size or col < 0 or col >= size:
                    print("Неверные координаты!")
                    continue
                
                if board[row][col] != ' ':
                    print("Клетка занята!")
                    continue
                
                board[row][col] = human_symbol
                
            except ValueError:
                print("Вводите только числа!")
                continue
        else:
            # Ход робота
            print(f"\nХод робота ({robot_symbol})")
            row, col = robot_move(board, robot_symbol)
            board[row][col] = robot_symbol
            print(f"Робот походил: {row}, {col}")
        
        # Показываем обновленное поле
        create_board(size, board)
        
        # Проверяем состояние игры
        if check_win(board, current_player):
            if current_player == human_symbol:
                print(f"Вы победили!")
            else:
                print(f"Робот победил!")
            winner = current_player
            game_over = True
        elif is_board_full(board):
            print("Ничья!")
            game_over = True
        else:
            # Меняем игрока
            current_player = 'O' if current_player == 'X' else 'X'
    
    return winner

def choose_mode():
    print("\nВыбери режим:")
    print("1. Игра с другом")
    print("2. Игра с ботом")
    
    while True:
        choice = input("Ваш выбор (1-2): ")
        if choice == '1':
            return 'друг'
        elif choice == '2':
            return 'бот'
        else:
            print("Введите 1 или 2!")

def play_game():
    mode = choose_mode()
    
    try:
        size = int(input("Размер поля (3-5): "))
        if size < 3 or size > 5:
            print("Размер должен быть от 3 до 5")
            return
    except:
        print("Введите число!")
        return
    
    first_player = random.choice(['X', 'O'])
    print(f"Первым ходит: {first_player}")
    
    if mode == 'friend':
        winner = play_with_friend(size, first_player)
    else:
        winner = play_with_robot(size, first_player)
    
    if winner is not None:
        save_stats(winner, mode)


while True:
    print("1. Новая игра")
    print("2. Статистика")
    print("3. Выход")
        
    choice = input("Выберите: ")
        
    if choice == '1':
        play_game()
    elif choice == '2':
        show_stats()
    elif choice == '3':
        print("До свидания!")
        break
    else:
        print("Неверный выбор")
