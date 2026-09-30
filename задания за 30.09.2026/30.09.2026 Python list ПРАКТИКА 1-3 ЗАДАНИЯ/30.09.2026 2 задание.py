requests = ["ПК-1", "ПК-2", "ПК-3"]
requests.append("ПК-4")
requests.insert(0, "Срочно")
index = requests.index("ПК-2")
requests[index] = "ПК-2 исправлен"
requests.remove("ПК-3")
popped_element = requests.pop()
print("Извлечённое значение:", popped_element)
print("Оставшийся список:", requests)