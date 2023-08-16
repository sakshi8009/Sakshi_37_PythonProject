def vowels(inputs):
    vowels = "AEIOUaeiou"
    result=set([each for each in vowels if each in inputs])
    return result

def main():
    inputs = input("Enter the string :")
    result = vowels(inputs)
    print("Vowels present :", result)
    print("Count of vowels :",len(result))

main()