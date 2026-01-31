def sort(array):
    arr = list(array)
    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] < arr[i-1]:
            for b in range(i, 0, -1):
                if arr[b] < arr[b-1]:
                    temp = arr[b]
                    arr[b] = arr[b-1]
                    arr[b-1] = temp
                else:
                    break
    return arr

def run_sorting():
    unsorted = [1, 3, 7, 8, 23, 0, 4, 5, 6, 2, 12]
    print(f"Unsorted list: {unsorted}")
    sorted_list = sort(unsorted)
    print(f"Sorted list:   {sorted_list}")

if __name__ == "__main__":
    run_sorting()
