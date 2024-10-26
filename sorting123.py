unsorted = [1,3,7,8,23,0,4,5,6,2,12]

def sort(array):
    for i in range(len(array)):
        if i == 0:
            pass
        if array[i]<array[i-1]:
            for b in range(i,0,-1):
                if array[b]<array[b-1]:
                    temp=array[b]
                    array[b]=array[b-1]
                    array[b-1]=temp
    return array

print(sort(unsorted))