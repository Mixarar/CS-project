import os


def search(search_item, search_array):
    while True:
        array_length = len(search_array)
        if array_length == 0:
            return False
        midpoint = array_length // 2

        if search_array[midpoint] == search_item:
            return True
        elif array_length <= 1:
            return False
        elif search_item > search_array[midpoint]:
            search_array = search_array[midpoint+1:]
        else:
            search_array = search_array[0:midpoint]


def sort(sort_array):
    array = list(sort_array)
    changed = True
    while changed:
        changed = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                changed = True
    return array


def run_search_hard():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(BASE_DIR, "data.txt")

    try:
        with open(data_file, "r") as f:
            content = f.read().strip()
            if content:
                farray = content.split(',')
                farray = [int(i.strip()) for i in farray]
            else:
                farray = []

        sorted_array = sort(farray)
        print("Sorted array:", sorted_array)

        try:
            item_s = int(
                input("Enter a number to search for (Binary Search): "))
        except ValueError:
            print("Invalid input. Searching for 11.")
            item_s = 11

        if search(item_s, sorted_array):
            print(f"Item {item_s} found!")
        else:
            print(f"Item {item_s} not found!")
    except FileNotFoundError:
        print(f"Error: {data_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_search_hard()
