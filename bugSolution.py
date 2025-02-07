def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

result = my_function(10, 0)
print(result) # Output: Error: Division by zero