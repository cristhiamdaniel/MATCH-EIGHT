from functions import *
import time
import pandas as pd
def findPairs1(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    :param arr:  List of elements
    :param sum: Sum of elements
    :return: List of pairs
    '''
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs

def findPairs2(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    using quick sort and binary search
    :param arr:
    :param sum:
    :return:
    '''
    pairs = []
    arr = quickSort(arr)
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

def findPairs3(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    using sorted function and binary search
    :param arr: List of elements
    :param sum: Sum of elements
    :return: List of pairs
    '''
    pairs = []
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

def findPairs4(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    using merge sort and binary search
    :param arr: List of elements
    :param sum: Sum of elements
    :return: List of pairs
    '''
    pairs = []
    arr = merge_sort(arr)
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

def findPairs5(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    using count sort and binary search
    :param arr: List of elements
    :param sum: Sum of elements
    :return: List of pairs
    '''
    pairs = []
    arr = counting_sort(arr, max(arr))
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

def findPairs6(arr, sum):
    '''
    Objective: To find pairs of elements in a list whose sum is equal to a given number
    using dynamic programming
    :param arr: List of elements
    :param sum: Sum of elements
    :return: List of pairs
    '''
    pairs = []
    numbers_viewed = {}
    for num in arr:
        missing_number = sum - num
        if missing_number in numbers_viewed:
            pairs.append((num, missing_number))
        else:
            numbers_viewed[num] = True
    return pairs

def main():
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    times5 = []
    times6 = []
    n = []
    sum = 0
    N = 100
    for i in range(1, N + 1):
        arr = generateRandomList(i)
        n.append(i)

        start = time.perf_counter()
        findPairs1(arr, sum)
        end = time.perf_counter()
        times1.append(end - start)

        arr = generateAscendingList(i)

        start = time.perf_counter()
        findPairs2(arr, sum)
        end = time.perf_counter()
        times2.append(end - start)

        start = time.perf_counter()
        findPairs3(arr, sum)
        end = time.perf_counter()
        times3.append(end - start)

        arr = generateDescendingList(i)

        start = time.perf_counter()
        findPairs4(arr, sum)
        end = time.perf_counter()
        times4.append(end - start)

        arr = generateRandomList(i)

        start = time.perf_counter()
        findPairs5(arr, sum)
        end = time.perf_counter()
        times5.append(end - start)

        start = time.perf_counter()
        findPairs6(arr, sum)
        end = time.perf_counter()
        times6.append(end - start)

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs[0, 0].scatter(n, times1)
    axs[0, 0].set_title('Function 1')
    axs[0, 0].grid()
    axs[0, 1].scatter(n, times2)
    axs[0, 1].set_title('Function 2')
    axs[0, 1].grid()
    axs[0, 2].scatter(n, times3)
    axs[0, 2].set_title('Function 3')
    axs[0, 2].grid()
    axs[1, 0].scatter(n, times4)
    axs[1, 0].set_title('Function 4')
    axs[1, 0].grid()
    axs[1, 1].scatter(n, times5)
    axs[1, 1].set_title('Function 5')
    axs[1, 1].grid()
    axs[1, 2].scatter(n, times6)
    axs[1, 2].set_title('Function 6')
    axs[1, 2].grid()
    plt.show()


    df = pd.DataFrame({'n': n, 'findPairs1': times1, 'findPairs2': times2, 'findPairs3': times3, 'findPairs4': times4,
                       'findPairs5': times5, 'findPairs6': times6})
    print(df)

    print()


if __name__ == '__main__':
    main()