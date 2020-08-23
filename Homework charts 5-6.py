######5-1#######

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

toy = 'doll'
print("\nIs toy == 'doll'? I predict True.")
print(toy == 'doll')
print("\nIs toy == 'car'? I predict False.")
print(toy=='car')


print("########5-2###############")
#Tests for equality and inequality with strings
# Tests using the lower() function
# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

pizza = 'Mozzarella'
print(pizza.lower()== 'mozzarella')
print(pizza == 'Mozarela')

age_V=27
age_B=32
print(age_V<=30 and age_B>=30)
print(age_V == age_B)
print(age_V>age_B)
print((age_B>age_V))
print(age_V>=30 or age_B>=30)
print('________________')

students = ['anna', 'vadim', 'olya', 'vasya']
print('olya' in students)
print('katya' in students)

student = 'katya'
if student not in students:
    print("We appologize")


print("###############5-3#################")
for x in range(2):
    alien_colors = ['red', 'green', 'yellow']
    # alien_colors = input("Enter alien color:")
    if 'green' in alien_colors:
        print("You just earned 5 points.")
    else:
        print()

print("###################5-4##################")
alien_colors = ['red', 'green', 'yellow']
# alien_colors = input("Enter alien color:")
if 'green' == alien_colors:
    print("You just earned 5 points.")
elif 'red' == alien_colors or 'yellow' == alien_colors:
    print("You just earned 10 points.")

# alien_colors = input("Enter alien color:")
if 'green' in alien_colors:
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")


print("####################5-5#################")
# for x in range(3):
#     alien_colors = ['red', 'green', 'yellow']
#     # alien_colors = input("Enter alien color:")
#     if 'green' == alien_colors:
#         point = 5
#     elif 'yellow' == alien_colors:
#         point = 10
#     elif 'red' == alien_colors:
#         point = 15
#     print("You just earned " + str(point) + " points.")

print("#####################5-6#################")
# for y in range(6):
#     # age = int(input("Enter your age:"))
#     if age < 2:
#         print("You are a baby .")
#     elif age < 4:
#         print("You are a toddler.")
#     elif age < 13:
#         print("You are a kid.")
#     elif age < 20:
#         print("You are a teenager.")
#     elif age < 65:
#         print ("You are an adult.")
#     elif age >= 65:
#         print("You are an elder. ")

print("##########################5-7################")
favorite_fruits = ['bananas', 'mango', 'avocado']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mango!")
if 'avocado' in favorite_fruits:
    print("You really like avocado!")
if 'mellon' in favorite_fruits:
    print("You really like mellon!")
if 'orange' in favorite_fruits:
    print("You really like orange!")

print("########################5-8###########")
users = ['eric', 'mathew', 'ivan', 'admin', 'xenia']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

print("#################5-9################")
if users:
    print(f"Hello, thank you for logging in again.")
else:
    print("We need to find some users!")

print("###################5-10##############")
new_users = ['admin', 'katy', 'julia', 'ivan', 'tim']
for user in new_users:
    if user in users:
        print(f"{user.title()}, you need to enter a new username .")
    else:
        print(f"The {user.title()} username is available!")

print("####################5-11##############")
for num in range(10):
    if num > 3:
        print(f"{num}th")
    elif num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")

print("################6-1###############")
husband = {'first_name': 'Vadzim', 'last_name': 'Bely', 'age' : 32, 'city' : 'Brooklyn'}
print(husband)
print('My husband is: ' + husband['first_name'], husband['last_name'] + '.')
print('He has ' + str(husband['age']) + ' years old.')
print('He lives in ' + husband['city']+ ' almost 4 years.')

print("##################6-2###############")
fav_num = {'mama': 7, 'Vadim': 5, 'Leon': 14, 'Viola': 27}
for key, value in fav_num.items():
    print(key + "'s favorite number is " + str(value) + ".")

print("###################6-3##############")
print('My lucky number: ' + '\n' + '\t' + '\t' + str(fav_num['mama']))

print("##########################")
numbers = list(range(1,11))
for number in numbers:
    for multi in numbers:
        print(f"{number}*{multi}={multi*number}")