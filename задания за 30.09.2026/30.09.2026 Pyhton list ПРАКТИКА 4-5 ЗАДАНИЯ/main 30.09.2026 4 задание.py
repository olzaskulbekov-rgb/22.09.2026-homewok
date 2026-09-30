def read_scores(count):
    scores = []
    while len(scores) < count:
        current_number = len(scores) + 1
        user_input = input(f"Введите оценку №{current_number}: ")
        try:
            score = int(user_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Ошибка: оценка должна быть в диапазоне от 0 до 100.")
        except ValueError:
            print("Ошибка: введите целое число.")
    return scores
if __name__ == "__main__":
    result = read_scores(5)
    print("Итоговый список оценок:", result)




