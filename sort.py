def insertion_sort(x):
    """
    Insertion sort is an in place sorting algorithm.
    Worst Case: O(n^2) - Input in reverse order
    Best Case: O(n) 
    Memory: O(1)
    """
    counter = 0

    n = len(x)
    for i in range(n):
        curr_index = i
        while curr_index > 0 and x[curr_index] < x[curr_index - 1]:
            counter += 1
            x[curr_index], x[curr_index - 1] = x[curr_index - 1], x[curr_index]
            curr_index = curr_index - 1
    print()
    print("Length of array:", n)
    print("Runtime:", counter)

def bubble_sort(x):
    """
    Bubble sort is in place, 
    Worst Case: O(n^2) 
    Best Case: O(n)
    Memory: O(1)
    """
    n = len(x)
    iterations = 0
    complete = False

    while complete == False:
        complete = True
        for i in range(n - iterations):
            if i > 0 and i < x[i] < x[i-1]:
                complete = False
                x[i], x[i-1] = x[i-1], x[i]
        iterations += 1
    
    return x

def selection_sort(x):
    """
    Selection sort is in place. 
    Worst Case: O(n^2)
    """

    n = len(x)
    min_index = 0
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if x[j] < x[min_index]:
                min_index = j 
        #Swap next lowest element to correct place
        x[i], x[min_index] = x[min_index], x[i]
        # print(x[0:i + 1], x[i + 1:])
    
def merge_sort(x):
    n = len(x)
    merge_sort_helper(x, 0, n - 1)

def merge_sort_helper(x, low, high):

    #Indicates that the 
    if low < high:
        mid = (low + high) // 2
        left = merge_sort_helper(x, low, mid)
        right = merge_sort_helper(x, mid + 1, high)
        # print("Left: ", left)
        # print("Right: ", right)
        # print("Sorted: ", merge(left, right))
        return merge(left, right)
    #Now low would be equal to high
    return [x[low]]

def merge(a, b):
    # O(a + b)
    a_index = 0
    b_index = 0
    c = []

    while a_index != len(a) or b_index != len(b): 
        if b_index == len(b):
            c.append(a[a_index])
            a_index += 1
        elif a_index == len(a):
            c.append(b[b_index])
            b_index += 1
        elif a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index += 1
        else: 
            c.append(b[b_index])
            b_index += 1
    return c


if __name__=="__main__":
    x = [4	,33	,84	,77	,77	,76	,71	,75	,96	,34	,81,	87,	13	,72,	90]
    selection_sort(x)
    # print(x)
    a = [1, 4, 6, 8, 9, 2,3,4,5,10]
    # b = [4, 222, 10, 2]
    merge_sort(a)
    



