import os

# exersice>>1

# with open('my_file.txt', 'w') as f:
#     f.write('first file handling in python\n')
#     f.write('second string 56rdx#$%\n')


# exersice>>2

# with open('sample.txt', 'r') as f:
#     file_contents = f.read()
#
# print(file_contents)


# exersice>>3

# with open('texty.txt', 'r') as file:
#     line_count = sum(1 for line in file)
#
# print(line_count)





# exersice>>4

# def count_words():
#     with open('stringy.txt', 'r') as file:
#         text = file.read()
#         words = text.split()
#         return len(words)
#
# print(count_words())




# exersice>>5

# file_name = "any_file.txt"
#
# with open(file_name, 'r') as foo:
#     buzz = foo.read()
#     char = len(buzz)
#
# print(char)



# exersice>>6

# with open('other.txt', 'r') as firstfile, open('another.txt', 'w') as secondfile:
#     for line in firstfile:
#         secondfile.write(line)



# exersice>>7

# def existing_func(smth):
#     with open('my_file.txt', 'a') as file:
#         file.write(smth)
# existing_func('HELLO WORLD')




# exersice>>8

# def renaming_func(old_name, new_name):
#     os.rename(old_name, new_name)
#
# renaming_func('old.txt', 'new.txt')





# exersice>>9

# def delete_file(file_path):
#     try:
#         os.remove(file_path)
#         print(f"File '{file_path}' deleted successfully.")
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#     except PermissionError:
#         print(f"Permission denied: Unable to delete file '{file_path}'.")
#
# # Example usage:
# delete_file('onlyFur_del.txt')







# exersice>>10
# def search_string(bar):
#     x = 0
#     y = []
#
#     with open('other.txt', 'r') as ree:
#         for line in ree:
#             x += 1
#             if bar in line:
#                 y.append((x, line.rstrip()))
#     return y
# print(search_string('h'))