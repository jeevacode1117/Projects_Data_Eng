my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3)
my_set = {1, 2, 10}
my_dict = {
    "NAME": "JEEVA",
    "AGE": 28,
    "SALARY": 75000,
}
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))
# Assign multiple values in a single line
x, y, z = 10, 20, 30
print(x)
#Dynamic Typing in Python
x=50
x="Hellow"
print(type(x));


basic_salary=85000
bonus = 25000
total_salary = basic_salary + bonus
print("Over_all_salary",total_salary);

#findremainder 

total_rolls=105
no_boxs=10
balance_roll = total_rolls%no_boxs
print("Balance_rolls",balance_roll);

print("Hello");

import sys

full_name = sys.argv[1]
print("Hello", full_name)
print("Hello", full_name, "Welcome to Python Programming")  
print(len(full_name))



