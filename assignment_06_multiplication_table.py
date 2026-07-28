def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        print(f"{number}  x  {multiplier}  =  {number * multiplier}")


def print_tables_up_to(limit):
    for number in range(1, limit + 1):
        print(f"Multiplication Table for {number}:")
        for multiplier in range(1, 13):
            print(f"{number}  x  {multiplier}  =  {number * multiplier}")
        if number < limit:
            print("-" * 27)


def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if number <= 0:
        print("Error: N must be a positive integer.")
        return

    print_single_table(number)

    try:
        limit = int(input("Enter a number N: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if limit <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to(limit)


if __name__ == "__main__":
    main()

