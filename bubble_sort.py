import random


def generate_random_numbers(start, finish, n):
    """Generates n random numbers ranging from the 'start' value to the 'finish' value"""
    numbers_list = [random.randint(start, finish) for _ in range(n)]
    return numbers_list


def bubble_sort(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - i - 1):
            if numbers_list[j] > numbers_list[j+1]:
                (numbers_list[j], numbers_list[j+1]) = (numbers_list[j + 1], numbers_list[j])
    return numbers_list


def reverse_bubble_sort(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list)-1, i, -1):
            if numbers_list[j] > numbers_list[j-1]:
                (numbers_list[j], numbers_list[j - 1]) = numbers_list[j-1], numbers_list[j]
    return numbers_list


if __name__ == '__main__':
    numbers_list = generate_random_numbers(0, 100, 10)
    print(bubble_sort(numbers_list))
    numbers_list = generate_random_numbers(0, 100, 10)
    print(reverse_bubble_sort(numbers_list))
