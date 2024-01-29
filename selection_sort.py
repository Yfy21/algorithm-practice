import random

numbers_list = [random.randint(1, 100) for _ in range(10)]


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
    for i in range(len(numbers_list)):
        current_smallest = numbers_list[0]
        current_smallest_index = 0
        for j in range(len(numbers_list)-i):
            if numbers_list[j] < current_smallest:
                current_smallest = numbers_list[j]
                current_smallest_index = j
        (numbers_list[-i-1], numbers_list[current_smallest_index]) = numbers_list[current_smallest_index], numbers_list[-i-1]
    return numbers_list


if __name__ == '__main__':
    print(selection_sort(numbers_list))
    # print(reverse_selection_sort(numbers_list))
