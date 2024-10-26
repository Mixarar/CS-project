def search(search_item,search_array):
    id_item=0
    for item in search_array:
        if int(item) == search_item:
            return id_item, item, True
        if item == search_item:
            return id_item, item, True
        else:
            id_item++1
    return False
        

f = open("data.txt", "r")
farray = f.read().split(',')
item_s = 10
print(farray)

if search(item_s,farray):
    print("Item found! The item searched is:", item_s)
else:
    print("item", item_s, "not found!")