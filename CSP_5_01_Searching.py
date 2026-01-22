import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    while True:
        x = random.randint(0, len(items)-1)
        if items[x] == target:
            return x
        else:
            pass


def linearSearch(items:list, target) -> tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    counter = 0
    for i in items:
        if i == target:
            return counter, counter + 1
        else:
            counter += 1
    return -1, len(items)


def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements binary search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    counter = 0
    up = len(items) - 1
    low = 0
    while low <= up:
        counter += 1
        mid = (up + low) // 2
        if items[mid] == target:
            return mid, counter
        elif target < items[mid]:
            up = mid - 1
        elif target > items[mid]:
            low = mid + 1
    return -1, counter