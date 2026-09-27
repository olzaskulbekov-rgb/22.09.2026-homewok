def trip_cost(distance, is_student):
    total = distance * 60
    if is_student:
        total = total * 0.8
        return total
print("Поездка студентов EKEB")
print("Без скидки:", trip_cost(10, False))
print("Со скидкой:", trip_cost(10, True))
print("Нулевое расстояние:", trip_cost(0, True))
