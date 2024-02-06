from typing import List, Union

def count_element_lengths(arr: List[Union[str, int]]) -> List[int]:
    return [len(str(element)) for element in arr]

string_array = ["abc", "apple", "orange"]
integer_array = [12, 456, 9000]

result_string = count_element_lengths(string_array)
result_integer = count_element_lengths(integer_array)

print(f"Input: {string_array}")
print(f"Output: {result_string}")

print(f"\nInput: {integer_array}")
print(f"Output: {result_integer}")