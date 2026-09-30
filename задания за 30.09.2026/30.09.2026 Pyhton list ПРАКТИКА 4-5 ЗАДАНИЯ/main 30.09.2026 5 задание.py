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
                print("Ошибка: оценка должна быть от 0 до 100.")
        except ValueError:
            print("Ошибка: введите целое число.")
    return scores
def show_statistics(scores):
    if not scores:
        print("Нет результатов")
        return
    total_count = len(scores)
    total_sum = sum(scores)
    average = round(total_sum / total_count, 2)
    minimum = min(scores)
    maximum = max(scores)
    passed = 0
    others = 0
    for score in scores:
        if score >= 70:
            passed += 1
        else:
            others += 1
    print(f"Количество: {total_count}")
    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Прошли (>=70): {passed}")
    print(f"Остальные (<70): {others}")
if __name__ == "__main__":
    scores_list = read_scores(5)
    print("\n--- Статистика ---")
    show_statistics(scores_list)