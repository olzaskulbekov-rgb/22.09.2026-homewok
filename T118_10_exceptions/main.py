def share_cost(total, people):
    return total / people
def read_integer(prompt, minimum):

    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value < minimum:
                print(f"Значение должно быть не меньше {minimum}")
            else:
                return value
        except ValueError:
            print("Введите целое число")
total = read_integer("Стоимость поездки, тенге: ", 0)
people = read_integer("Количество участников: ", 1)
result = share_cost(total, people)
print("С каждого участника:", round(result, 2), "тенге")







