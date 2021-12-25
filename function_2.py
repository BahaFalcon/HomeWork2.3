import random

a = 1
b = 101
q = 7

def another_func(func):
    def other_func():
        for i in range(7):
            func()
    return other_func

@another_func
def a_func():
    nums = random.randint(a, b)
    print(f'Ваше случайное число: {nums}')

if __name__ == '__main__':
    print(a_func())