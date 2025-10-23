import array as arr

def BubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
                if array[j]>array[j+1]:
                   temp=array[j]
                   array[j]=array[j+1]
                   array[j+1]=temp
    return array  

array=arr.array('i',[64, 34, 25, 12, 22, 11, 90])
print("Unsorted array is:",array)   
print("Sorted Array: ",BubbleSort(array))                    
                       
