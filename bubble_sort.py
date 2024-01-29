import random

numbers_list = [random.randint(1, 100) for _ in range(10)]


def bubble_sort(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - i - 1):
            if numbers_list[j] > numbers_list[j+1]:
                (numbers_list[j], numbers_list[j+1]) = (numbers_list[j + 1], numbers_list[j])
    return numbers_list


def reverse_bubble_sort(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list)-1, i, -1):
            if numbers_list[j] < numbers_list[j-1]:
                (numbers_list[j], numbers_list[j - 1]) = numbers_list[j-1], numbers_list[j]
    return numbers_list


if __name__ == '__main__':
    print(bubble_sort(numbers_list))
    # print(reverse_bubble_sort(numbers_list))
