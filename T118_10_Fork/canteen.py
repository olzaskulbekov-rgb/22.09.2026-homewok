def lunch_cost(total):
    if total > 3000:
        return total - 300
    return total
print("Сумма 0:", lunch_cost(0))
print("Сумма 2999:", lunch_cost(2999))
print("Сумма 3000:", lunch_cost(3000))
print("Сумма 3001:", lunch_cost(3001))
