import array as arr

def InsertionSort(array):
    for i in range(1,len(array)):
        current=array[i]
        j=i-1
        while j>=0 and array[j]>current:
            array[j+1]=array[j]
            j-=1
        array[j+1]=current
    return array

array=arr.array("i",[25,78,45,13,20,79,24])
print("Before Sort: ",array)
print("After InsertionSort: ",InsertionSort(array))
