import random

random.seed(10)  # явно устанавливаем начальное значение для генератора случайных чисел

numbers = [random.randrange(1, 50) for _ in range(7)]

if __name__ == '__main__':
    print(*sorted(numbers))


