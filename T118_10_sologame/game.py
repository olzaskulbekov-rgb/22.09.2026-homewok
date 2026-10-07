def show_rules():
    print("\n" + "=" * 45)
    print("=== Правила игры 'Забери последние камни' ===")
    print("=" * 45)
    print("1. В начале игры в куче 15 камней.")
    print("2. Игрок и компьютер ходят по очереди. Первым ходит игрок.")
    print("3. За один ход можно взять от 1 до 3 камней, но не больше остатка.")
    print("4. Компьютер всегда берет 1 камень.")
    print("5. Побеждает тот, кто заберет последний камень!")
    print("=" * 45 + "\n")


def can_take(amount, stones):

    return 1 <= amount <= 3 and amount <= stones


def take_stones(stones, amount):

    if can_take(amount, stones):
        return stones - amount
    return stones


def computer_move(stones):

    if stones > 0:
        return 1
    return 0


def option_choice(prompt, allowed):

    while True:
        user_input = input(prompt).strip()
        if user_input in allowed:
            return user_input
        print(f"Некорректный ввод! Пожалуйста, выберите одно из следующих значений: {', '.join(allowed)}")


def play_game():

    stones = 15
    print("\n Начало новой игры! ")

    while stones > 0:

        allowed_moves = [str(i) for i in range(1, 4) if i <= stones]

        prompt = f"Ваш ход (осталось {stones} камней, можно взять {', '.join(allowed_moves)}): "
        player_choice_str = option_choice(prompt, allowed_moves)
        player_choice = int(player_choice_str)


        stones = take_stones(stones, player_choice)
        print(f"Вы взяли {player_choice} stone(s). Осталось камней: {stones}")


        if stones == 0:
            print("\n Поздравляем! Вы забрали последний камень и победили!\n")
            return


        comp_choice = computer_move(stones)
        stones = take_stones(stones, comp_choice)
        print(f"Компьютер взял {comp_choice} stone(s). Осталось камней: {stones}\n")


        if stones == 0:
            print("\n Компьютер забрал последний камень. Вы проиграли!\n")
            return


def main():

    while True:
        print("=== ГЛАВНОЕ МЕНЮ ===")
        print("1 - Начать игру")
        print("2 - Правила")
        print("0 - Выход")

        choice = option_choice("Выберите действие: ", ["1", "2", "0"])

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("Спасибо за игру! До свидания.")
            break


if __name__ == "__main__":
    main()