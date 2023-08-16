def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

def main():
    num_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    unique_numbers = remove_duplicates(num_list)

    print("Unique numbers:", unique_numbers)

main()