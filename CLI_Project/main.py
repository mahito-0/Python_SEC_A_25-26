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


def clean_name(name: str) -> str:
    return name.strip().title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if max_val is not None and val > max_val:
            print(f"Input must be less than or equal to {max_val}.")
            continue
        if val < min_val:
            print(f"Input must be greater than or equal to {min_val}.")
            continue
        return val
    
def garde_from_percentage(percentage: float) -> str:
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
    
def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

def add_student(students: list[dict]) -> None:
    sid = prompt_on_empty("Enter student ID: ")
    name = clean_name(prompt_on_empty("Enter student name: "))
    
    n = prompt_int("Enter number of subjects: ", min_val=1)
    
    subjects: list[str] = []
    marks: list[float] = []
  
    for i in range(n):
        sub = prompt_on_empty(f"Enter subject {i+1} name: ")
        subjects.append(sub)
        
        marks.append(prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0))
        
    
    total, pct = compute_total_and_percentage(marks)
    grade = garde_from_percentage(pct)
    status = "Pass" if grade != "F" else "Fail"

    student = {
        "id": sid,
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "percentage": pct,
        "grade": grade,
        "Status": status
    }
    
    students.append(student)
    
    
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