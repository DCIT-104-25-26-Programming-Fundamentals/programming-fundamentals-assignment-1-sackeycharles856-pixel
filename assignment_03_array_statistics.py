def calculate_sum(numbers):
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
    return maximum


def calculate_minimum(numbers):
    minimum = numbers[0]
    for value in numbers[1:]:
        if value < minimum:
            minimum = value
    return minimum


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for index in range(1, count + 1):
        try:
            value = int(input(f"Enter number {index}: "))
        except ValueError:
            print("Error: Please enter valid integers.")
            return
        numbers.append(value)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {calculate_maximum(numbers)}")
    print(f"Minimum: {calculate_minimum(numbers)}")


if __name__ == "__main__":
    main()

