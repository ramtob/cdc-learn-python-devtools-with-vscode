def fibonacci(n): 
    a, b = 0, 1 
    result = [] 
    for _ in range(n): 
        result.append(a)  # Set a breakpoint here 
        a, b = b, a + b  # Set a breakpoint here 
    return result 

# Testing the fibonacci function 
print(fibonacci(5))  # Output should be [0, 1, 1, 2, 3] 