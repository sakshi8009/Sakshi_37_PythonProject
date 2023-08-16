def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        
        numbers[j + 1] = key

def main():
    num_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    insertion_sort(num_list)

    print("Sorted numbers:", num_list)

main()