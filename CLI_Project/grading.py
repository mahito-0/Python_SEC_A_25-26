"""
this module contains the grading system for the CLI project. It provides functionality to calculate grades based on student scores and to determine the corresponding letter grades.
"""

from __future__ import annotations


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