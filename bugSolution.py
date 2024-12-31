def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (this will now return 0):
my_list = []
average = calculate_average(my_list)
print(average)  # Output: 0

#Example with numbers
my_list = [10,20,30,40,50]
average = calculate_average(my_list)
print(average) # Output: 30.0