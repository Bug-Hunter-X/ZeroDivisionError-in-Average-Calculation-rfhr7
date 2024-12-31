This repository contains a Python code example that demonstrates a common programming error: a `ZeroDivisionError`. The `calculate_average` function attempts to compute the average of a list of numbers, but it fails when given an empty list, resulting in division by zero.  The solution demonstrates how to handle this situation gracefully by adding error handling (checking for an empty list) before performing the calculation. The solution shows best practice by returning 0 for an empty list, instead of crashing.