import os

# Add subdirectories to sys.path to allow imports if needed,
# but for simple execution, we can just import the run functions.

from algorithms.search import run_search
from algorithms.search_hard import run_search_hard
from algorithms.sorting123 import run_sorting
from booking_system.booking import run_booking_system
from data_structures.linkedlist import run_linkedlist_demo
from data_structures.stack import run_stack_demo
from high_scores.high_scores import run_high_scores
from shapes.shapes import run_shapes_demo
from student_management.con import run_student_demo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_choice():
    print("\n" + "=" * 30)
    print("      CS PROJECT MAIN MENU      ")
    print("=" * 30)
    print("1. Transport Booking System")
    print("2. High Scores Tracker")
    print("3. Student Management Demo")
    print("4. Shapes Area Calculation")
    print("5. Linked List Demo")
    print("6. Stack Demo")
    print("7. Simple Search")
    print("8. Binary Search (Hard Search)")
    print("9. Sorting Demo")
    print("0. Exit")
    print("=" * 30)
    return input("Select an option (0-9): ")


def main_menu():
    actions = {
        '1': run_booking_system,
        '2': run_high_scores,
        '3': run_student_demo,
        '4': run_shapes_demo,
        '5': run_linkedlist_demo,
        '6': run_stack_demo,
        '7': run_search,
        '8': run_search_hard,
        '9': run_sorting
    }
    while True:
        choice = get_choice()
        if choice == '0':
            print("Exiting... Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice, please try again.")

        input("\nPress Enter to return to the menu...")
        clear_screen()


if __name__ == "__main__":
    main_menu()
