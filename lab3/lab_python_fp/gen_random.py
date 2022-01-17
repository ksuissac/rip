# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
    # Необходимо реализовать генератор
import random
def gen_random(num_count, first, last):
    for number in range(num_count):
        yield random.randint(first, last)

for i in gen_random(5, 1, 3):
        print(i)