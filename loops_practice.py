# loops_practice.py

# --- Блок данных (как просили в задании) ---
numbers = list(range(1, 8))
words = [f"str{i}" for i in range(10)]

# --- Задача 1: Список чисел ---
for n in numbers:
    print(n)
    if n == 5:
        break

# --- Задача 2: Список строк ---
for word in words:
    print(word)


