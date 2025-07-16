def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero"
        result /= num
    return result

def main():
    print("Simple Calculator (Any Number of Values)")
    count = int(input("How many numbers? "))
    numbers = []
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Reasult:", add(numbers))
    elif choice == '2':
        print("Result:", subtract(numbers))
    elif choice == '3':
        print("Result:", multiply(numbers))
    elif choice == '4':
        print("Result:", divide(numbers))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()