""" 
This module contains functions for processing student data.
"""
from __future__ import annotations
from utils import prompt_on_empty, clean_name, prompt_int, prompt_float
from grading import compute_total_and_percentage, garde_from_percentage

def print_student_report(students: list[dict]) -> None:
    print("----- Student Report -----")
    print("\n" + "-" * 50)
    print(f"Student Id: {students['id']}")
    print(f"Student Name: {students['name']}")
    print(f"Subjects: {', '.join(students['subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in students['marks'])}")
    print(f"Total Marks: {students['total']}")
    print(f"Percentage: {students['percentage']:.2f}%")
    print(f"Grade: {students['grade']}")
    print(f"Status: {students['Status']}")

    
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
    