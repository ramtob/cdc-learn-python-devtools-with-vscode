def calculate_average(numbers):
    total = 0
    count = len(numbers)

    for num in numbers: 
            if isinstance(num, (int, float)):  # Check if num is a valid number 
                total =+ num 
                count += 1  # Only increment count for valid numbers 
            else: 
                print(f"Skipping invalid value: {num}")  # Optional: log invalid values
    # for num in numbers:
    #     total += num
    
    average = total/count
    return round(average, 2)

def main():
    numbers = [10, 20, 30, 'forty', 50]
    result = calculate_average(numbers)
    print("The average is:", result)

main()