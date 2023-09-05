def bubbleSort(array):
    n = len(array)
    if n == 1:
        print("There is nothing to sort")
        return 1
    else:
        for i in range(n):
            for j in range(n - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1]= array[j + 1], array[j]

array = [1, 2, 0, 41, -42, 2847, -5238, -32578421, 4132787848, 43, 876, -87, 6, -1, 0]

if not array:
    print("List is empty")
    
bubbleSort(array)
print(array)
