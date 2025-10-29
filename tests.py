from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

""" 
print('Result for current directory:')
print(get_files_info("calculator", "."),'\n')

print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"),'\n')

print("Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"),'\n')

print("Result for '../' directory:")
print(get_files_info("calculator", "../"),'\n') 
"""

"""
print('Result for main.py file:')
print(get_file_content("calculator", "main.py"),'\n')

print('Result for pkg/calculator.py file:')
print(get_file_content("calculator", "pkg/calculator.py"),'\n')

print('Result for /bin/cat file:')
print(get_file_content("calculator", "/bin/cat"),'\n')

print('Result for pkg/does_not_exist.py file:')
print(get_file_content("calculator", "pkg/does_not_exist.py"),'\n') 
"""

print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))