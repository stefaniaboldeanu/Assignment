name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old".format(name,age))
print("My name is {} and I am {} years old.".format(name, age))
name2 = "Ioana"
age2= 55
print(f"My name is {name2} and I am {age2} years old")
print("My name is {} and I am {} years old".format(name2, age2))

import re
s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

s2 = "The BodyGuard is the best album of 'Whitney Houston'."


# Use the findall() function to find all occurrences of the "st" in the string
result = re.findall("st", s2)

# Print out the list of matched words
print(result)
print(type(result))

# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# Define the regular expression pattern to search for
pattern = r"Whitney Houston"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 
print("helloMike".find("Mike"))

A=((11,12),[21,22])
print(type(A))
a= A[0][1]
print(a)
L = ['c', 'd']
L.append(['a','b'])
print(L)
B=L
print(type(B))     
d= {"The Bodyguard":"1992", "Saturday Night Fever":"1977"} 
print(d.keys())
print(d.values())


# user_choice = "Withdraw Cash"
# if user_choice == "Withdraw Cash":
#     amount = int(input("Enter the amount to withdraw: "))
#     if amount % 10 == 0:
#         print("Amount dispensed: ", amount)
#     else:
#         print("Please enter a multiple of 10.")
# else:
#     print("Thank you for using the ATM.")



for x in range(0, 3):
    print(x)
    
for i, y in enumerate(['A', 'B', 'C']):
    print(i, y)