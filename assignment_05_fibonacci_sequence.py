def generate_fibonacci_terms(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]

    terms = [0, 1]
    while len(terms) < count:
        terms.append(terms[-1] + terms[-2])
    return terms


def print_fibonacci_sequence():
    try:
        count = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    terms = generate_fibonacci_terms(count)
    print("Fibonacci sequence:", " ".join(str(term) for term in terms))


def is_fibonacci_number(number):
    if number < 0:
        return False
    if number == 0:
        return True

    previous, current = 0, 1
    while current < number:
        previous, current = current, previous + current

    return current == number


def check_fibonacci_number():
    try:
        number = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    print_fibonacci_sequence()
    print()
    check_fibonacci_number()


if __name__ == "__main__":
    main()

