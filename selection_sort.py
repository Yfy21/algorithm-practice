import random


def generate_random_numbers(start, finish, n):
    """Generates n random numbers ranging from the 'start' value to the 'finish' value"""
    numbers_list = [random.randint(start, finish) for _ in range(n)]
    return numbers_list


def selection_sort(numbers_list):
    for i in range(len(numbers_list)):
        current_smallest = numbers_list[i]
        current_smallest_index = i
        for j in range(i+1, len(numbers_list)):
            if numbers_list[j] < current_smallest:
                current_smallest = numbers_list[j]
                current_smallest_index = j
        (numbers_list[i], numbers_list[current_smallest_index]) = numbers_list[current_smallest_index], numbers_list[i]
    return numbers_list


def reverse_selection_sort(numbers_list):
    current_loop = 1
    for i in range(len(numbers_list)-1, -1, -1):
        current_smallest = numbers_list[i]
        current_smallest_index = i
        for j in range(len(numbers_list)-1-current_loop, -1, -1):
            if numbers_list[j] < current_smallest:
                current_smallest = numbers_list[j]
                current_smallest_index = j
        (numbers_list[i], numbers_list[current_smallest_index]) = numbers_list[current_smallest_index], numbers_list[i]
        current_loop += 1
    return numbers_list


if __name__ == '__main__':
    numbers_list = generate_random_numbers(0, 100, 10)
    print(selection_sort(numbers_list))
    numbers_list = generate_random_numbers(0, 100, 10)
    print(reverse_selection_sort(numbers_list))
