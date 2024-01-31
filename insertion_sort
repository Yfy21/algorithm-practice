import random


def generate_random_numbers(start, finish, n):
    """Generates n random numbers ranging from the 'start' value to the 'finish' value"""
    numbers_list = [random.randint(start, finish) for _ in range(n)]
    return numbers_list


def insertion_sort(numbers_list):
    """Sorts a list of numbers in ascending order using insertion sort."""
    for i in range(len(numbers_list)):
        for j in range(i, 0, -1):
            if numbers_list[j] < numbers_list[j-1]:
                (numbers_list[j], numbers_list[j-1]) = numbers_list[j - 1], numbers_list[j]
            else:
                break
    return numbers_list


def reverse_insertion_sort(numbers_list):
    """Sorts a list of numbers in descending order using insertion sort."""
    for i in range(len(numbers_list)-2, -1, -1):
        for j in range(i, len(numbers_list)-1):
            if numbers_list[j] < numbers_list[j+1]:
                (numbers_list[j], numbers_list[j+1]) = numbers_list[j+1], numbers_list[j]
            else:
                break
    return numbers_list


if __name__ == '__main__':
    numbers_list = generate_random_numbers(0, 100, 10)
    print(insertion_sort(numbers_list))
    numbers_list = generate_random_numbers(0, 100, 10)
    print(reverse_insertion_sort(numbers_list))
