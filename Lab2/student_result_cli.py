'''
Asimple command-line interface (CLI) for managing student results. 
This CLI allows users to add, view, and manage student results in a straightforward manner.
'''

def prompt_on_empty(prompt: str) -> str:
    while True:
        s: str = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty. Please try again.")

def add_student(students: list[dict]) -> None:
    sid: str = prompt_on_empty("Enter student ID: ")
    name: str = prompt_on_empty("Enter student name: ")
    print(f"Student ID: {sid}")
    print(f"Student Name: {name}")
  
    
    
def print_menu() -> None:
    print("----- Student Result Calculator -----")
    print("1. Add Student + compute Result")
    print("2. List Students and Results")
    print("3. Search student by id")
    print("4. Delete student by id")
    print("5. Export results to CSV")
    print("6. Exit")
    
def main() -> None:
    students: list[dict] = [] #List to contain student
    while True:
        print_menu()
        choice: str = input("Chose an option (1-6): ").strip()
        #Match-case is only available in Python 3.10 
        match choice:
            case "1":
                add_student(students)
            case "2":
                print("Listing students and results...")
            case "3":
                print("Searching student by id...")
            case "4":
                print("Deleting student by id...")
            case "5":
                print("Exporting results to CSV...")
            case "6":
                print("Exiting the program. Goodbye!")    
                break
            case _:
                print("Invalid option. Please choose a number between 1 and 6.")
        
        
if __name__ == "__main__":
    main()