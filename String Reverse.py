
# my_reverse reverses a string
# input: a string
# output: the input string reverse
string_to_reverse = 'apples'
def my_reverse(string_to_reverse):
    reversed_string = ''
    for char in string_to_reverse:
        reversed_string =  char + reversed_string 
    return reversed_string
print(my_reverse(string_to_reverse))



# reverse_strings_in_list reverses all strings in a given list
# input: a list of strings
# output: a list of the strings reversed
list_of_strings = ["", "a", "apple", "racecar"]
def reverse_strings_in_list(list_of_strings):
    reversed_string_list = []
    for reverse in list_of_strings:
        reversed_string_list.append(my_reverse(reverse))
    return reversed_string_list
print(reverse_strings_in_list(list_of_strings))