import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def generateRandomList(n):
    '''
    Objective: To generate a list of random integers
    :param n: Number of elements in the list
    :return: A list of random integers
    '''
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 2*n))
    return arr

def generateDescendingList(n):
    '''
    Objective: To generate a list of descending integers
    :param n: Number of elements in the list
    :return: A list of descending integers
    '''
    arr = []
    for i in range(n):
        arr.append(n-i)
    return arr

def generateAscendingList(n):
    '''
    Objective: To generate a list of ascending integers
    :param n: Number of elements in the list
    :return: A list of ascending integers
    '''
    arr =[]
    for i in range(1,n+1):
        arr.append(i)
    return arr

def plotGraph(x, y, legend):
    '''
    Objective: To plot a graph
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param legend: Legend for the graph
    :return: None
    '''
    plt.plot(x, y, label=legend)
    plt.grid()

def binarySearch(arr, x):
    '''
    Objective: To search for an element in a list using binary search
    :param arr: List of elements
    :param x: Element to be searched
    :return: Index of the element if found, else False
    '''
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return True
    return False

def quickSort(arr):
    '''
    Objective: To sort a list using quick sort
    :param arr: List of elements
    :return: Sorted list
    '''
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

def merge_sort(lst):
    '''
    Objective: To sort a list using merge sort
    :param lst: List of elements
    :return: Sorted list
    '''
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    '''
    Objective: To merge two sorted lists
    :param left: List of elements
    :param right: List of elements
    :return: Sorted list
    '''
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def counting_sort(lst, max_val):
    '''
    Objective: To sort a list using counting sort
    :param lst: List of elements
    :param max_val: Maximum value in the list
    :return: Sorted list
    '''
    count = [0] * (max_val + 1)
    for val in lst:
        count[val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    result = [0] * len(lst)
    for val in lst:
        result[count[val] - 1] = val
        count[val] -= 1
    return result
def get_poly_fit(x,y,degree):
    '''
    Objective: To get a polynomial fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param degree:  Degree of the polynomial
    :return:  Polynomial fit
    '''
    z = np.polyfit(x,y,degree)
    f = np.poly1d(z)
    return f

def get_r2(x,y,degree):
    '''
    Objective: To get the r2 value
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param degree: Degree of the polynomial
    :return: r2 value
    '''
    f = get_poly_fit(x,y,degree)
    yhat = f(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y-ybar)**2)
    return ssreg/sstot

def plot_fit(x, y, title, x_label, y_label, degree):
    '''
    Objective: To plot a graph with a polynomial fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param title: Title of the graph
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :param degree: Degree of the polynomial
    :return: None
    '''
    f = get_poly_fit(x, y, degree)
    plt.plot(x, f(x), 'r--', label='fit: r2=%5.3f' % get_r2(x, y, degree))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()
def get_log_fit(x, y):
    '''
    Objective: To get a log fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :return: Log fit
    '''
    def func(x, a, b):
        return list(map(lambda n: n * a * np.log(n*b), x))
    popt, pcov = curve_fit(func, x, y)
    return func(x, *popt)

def get_r2_log(x, y):
    '''
    Objective: To get the r2 value
    :param x: List of x-coordinates
    :param y:  List of y-coordinates
    :return: r2 value
    '''
    yhat = get_log_fit(x, y)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    return ssreg / sstot

def plot_log_fit(x, y, title, x_label, y_label):
    '''
    Objective: To plot a graph with a log fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param title: Title of the graph
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: None
    '''
    f = get_log_fit(x,y)
    plt.plot(x, f, 'r--', label='fit: r^2=%5.3f' % get_r2_log(x, y))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()

def get_line_fit(x, y):
    '''
    Objective: To get a line fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :return: Line fit
    '''
    def func(x, a, b):
        return list(map(lambda n: n*a+b, x))
    popt, pcov = curve_fit(func, x, y)
    return func(x, *popt)

def get_r2_line(x, y):
    '''
    Objective: To get the r2 value
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :return: r2 value
    '''
    yhat = get_line_fit(x, y)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    return ssreg / sstot

def plot_line_fit(x, y, title, x_label, y_label):
    '''
    Objective: To plot a graph with a line fit
    :param x: List of x-coordinates
    :param y: List of y-coordinates
    :param title: Title of the graph
    :param x_label: Label for x-axis
    :param y_label: Label for y-axis
    :return: None
    '''
    f = get_line_fit(x, y)
    plt.plot(x, f, 'r--', label='fit: r^2=%5.3f' % get_r2_line(x, y))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid()
    plt.show()