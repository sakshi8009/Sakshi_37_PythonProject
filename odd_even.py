def check_odd_even(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return odd_numbers, even_numbers

def main():
    num_tuple = tuple(map(int, input("Enter a tuple of numbers separated by spaces: ").split()))
    odd_numbers, even_numbers = check_odd_even(num_tuple)

    print("Odd numbers:", odd_numbers)
    print("Even numbers:", even_numbers)

main()