f = open("data.txt", "r")
farray = f.read().split(',')
farray=[eval(i) for i in farray]

def search(search_item,search_array):
    while True:
        array_length = len(search_array)
        midpoint = int(array_length/2) - 1
        if array_length<=3:
            for i in search_array: 
                if i == search_item: return True
            return False
        elif search_item > search_array[midpoint]: search_array = search_array[midpoint:array_length]
        elif search_item < search_array[midpoint]: search_array = search_array[0:midpoint]
        elif search_item == search_array[midpoint]: return True
        else: return False
        
def sort(sort_array):
    changed = True
    while changed:
        changed = False
        for i in range(len(sort_array) - 1):
            if sort_array[i] > sort_array[i + 1]:
                temp = sort_array[i]
                sort_array[i] = sort_array[i + 1]
                sort_array[i + 1] = temp
                changed = True
            i += 1
    print(sort_array)



#print(sort(unsorted))
print(search(11,farray))