def calculate_total (a,b):
    total = a+b
    return total

result = calculate_total(5,7)
print(result)
string_length = len("Hello, World!")  
print(string_length)
list_length = len([1, 2, 3, 4, 5])
print(list_length)
total = sum([10, 20, 30, 40, 50]) 
print(total)
highest = max([5, 12, 8, 23, 16]) 
print(highest)
lowest = min([5, 12, 8, 23, 16])
print(lowest)

def function_name():
    pass # placeholder or a no-op (no operation) statement

# def greet(name):
#     return "Hello "+ name
# result=greet("Alina")
# print(result)

def greet(name):
    return "Hello, " + name
for _ in range(3):
    print(greet("Alice"))

my_list=[]
def add_element(data_structure, element):
    data_structure.append(element)
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)
print("Current list:", my_list)

a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a =", a)
except:
    print("There was an error")
