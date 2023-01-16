import random


def binary_search(data, target, low_index, high_index):
    if low_index > high_index:
        return False

    mid = (low_index + high_index) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        #recursive, until the lower index is equal to the higher index
        return binary_search(data, target, low_index, mid - 1) #left searching, from the middle to down
    else:
        #recursive, until the lower index is equal to the higher index
        return binary_search(data, target, mid + 1, high_index) #right searching, from the middle up


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input('What number would you like to find? '))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)