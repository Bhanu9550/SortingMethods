import array as arr

def SelectionSort(array):
    for i in range(0,len(array)-1):
        minindex=i
        for j in range(i+1,len(array)):
            if array[minindex]>array[j]:
                minindex=j
        temp=array[minindex]
        array[minindex]=array[i]
        array[i]=temp

    return array

array=arr.array('i',[64, 34, 25, 22, 78, 34, 23, 45, 99, 75, 11])
print("Unsorted array is:",array)
print("Sorted Array: ",SelectionSort(array))  