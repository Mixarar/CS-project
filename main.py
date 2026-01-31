import sys
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

def main_menu():
    while True:
        print("\n" + "="*30)
        print("      CS PROJECT MAIN MENU      ")
        print("="*30)
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
        print("="*30)
        
        choice = input("Select an option (0-9): ")

        if choice == '1':
            run_booking_system()
        elif choice == '2':
            run_high_scores()
        elif choice == '3':
            run_student_demo()
        elif choice == '4':
            run_shapes_demo()
        elif choice == '5':
            run_linkedlist_demo()
        elif choice == '6':
            run_stack_demo()
        elif choice == '7':
            run_search()
        elif choice == '8':
            run_search_hard()
        elif choice == '9':
            run_sorting()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        input("\nPress Enter to return to the menu...")
        clear_screen()

if __name__ == "__main__":
    main_menu()
