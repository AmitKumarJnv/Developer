# calculations.py
import logging

# Custom exception is still the best practice
class EmptyListError(Exception):
    pass

def calculate_mean(numbers):
    # Raise explicit errors. Do NOT handle them here.
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise EmptyListError("Cannot compute mean of an empty list")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All list elements must be numbers")
    
    return sum(numbers) / len(numbers)