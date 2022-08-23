import random


def make_list(n: int) -> list:
    return [i for i in range(n)]


def copy_list(arr: list) -> list:
    return [x for x in arr]


def my_sort(arr: list) -> list:
    new_arr = copy_list(arr)
    for i in range(len(new_arr) - 1):
        lowest_idx = len(new_arr) - 1
        for j in range(i, len(new_arr) - 1):
            if new_arr[j] < new_arr[lowest_idx]:
                lowest_idx = j
        lowest = new_arr.pop(lowest_idx)
        new_arr.insert(i, lowest)
    return new_arr


if __name__ == "__main__":

    arr = make_list(20)
    random.shuffle(arr)
    
    sorted_arr = my_sort(arr)

    print(arr)
    print(sorted_arr)
