from module_1.greet import greet
from module_2.calculate_square import calculate_square
from module_3.concatenate_strings import concatenate_strings

def main():
    print(greet())

    num = 5
    squared_result = calculate_square(num)
    print(f"The square of {num} is: {squared_result}")

    string1 = "Hello"
    string2 = "World!"
    concatenated_result = concatenate_strings(string1, string2)
    print(f"Concatenated String: {concatenated_result}")

if __name__ == "__main__":
    main()
