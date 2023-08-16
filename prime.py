def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

def extract_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

def main():
    num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    prime_numbers = extract_primes(num_list)
    
    print("Prime numbers in the list:", prime_numbers)

main()
