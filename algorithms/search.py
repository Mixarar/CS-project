import os


def search(search_item, search_array):
    id_item = 0
    for item in search_array:
        try:
            if int(item) == search_item:
                return id_item, item, True
        except ValueError:
            if item == search_item:
                return id_item, item, True
        id_item += 1
    return False


def run_search():
    # Get the directory of the current script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(BASE_DIR, "data.txt")

    try:
        with open(data_file, "r") as f:
            farray = f.read().split(',')

        # Clean up whitespace
        farray = [item.strip() for item in farray]

        print("Array content:", farray)

        try:
            item_s = int(input("Enter a number to search for: "))
        except ValueError:
            print("Invalid input. Searching for default item 10.")
            item_s = 10

        result = search(item_s, farray)
        if result:
            idx, val, found = result
            print(f"Item found! The item searched is: {val} at index {idx}")
        else:
            print(f"Item {item_s} not found!")
    except FileNotFoundError:
        print(f"Error: {data_file} not found.")


if __name__ == "__main__":
    run_search()
