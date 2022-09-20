#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name)
def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name('username')

#Question 2:Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    for num in range(0,101):
        if num % 2 == 1:
            print(num)

first_odds()

#Question 3:Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_a_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_a_list([1,10,2,9,18,11])
print(max_num_in_a_list([1,10,2,9,18,11]))

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year)
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(True)
    elif a_year % 400 == 0:
        print(True)
    else:
        print(False)

is_leap_year(2022)

#Question 5:Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
def is_consecutive(a_list):
    i = 0 
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i +1]:
            i += 1
        else:
            status = False
    print(status)
