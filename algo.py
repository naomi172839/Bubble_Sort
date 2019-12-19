from random import randint


def bubble_sort(unsorted_list):
    swapped = True
    iteration_count_1 = 1

    while swapped:
        swapped = False
        count_1 = 0
        iteration_count_1 += 1

        while count_1 < len(unsorted_list) - 1:
            if unsorted_list[count_1] > unsorted_list[count_1 + 1]:
                swapped = True
                temp_1 = unsorted_list[count_1]
                temp_2 = unsorted_list[count_1 + 1]
                unsorted_list[count_1] = temp_2
                unsorted_list[count_1 + 1] = temp_1
            count_1 += 1

    return iteration_count_1 , unsorted_list


def create_random_list():
    random_list = []
    for i in range(randint(2, 10000)):
        random_list.append(randint(randint(-10000,0), randint(0, 10000)))

    return random_list


i_count, sorted_list = bubble_sort(create_random_list())
print("Total Loops: " + str(i_count))
print("Length of List: " + str(len(sorted_list)))
print("Sorted List: ")
print(sorted_list)