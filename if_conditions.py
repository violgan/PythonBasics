cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# is_bmw_listed=('bmw' in cars)
# print(is_bmw_listed)
# print('bmw' in cars)
#
# if('bmw5' not in cars):
#     cars.append('bmw5')
# print(cars)
# for car in cars:
#     if 'bmwx5' != car.lower():
#         print(f"{car} is not bmwx5")
# print(cars)
# status=False
# if status:
#     print('it is true')
# else:
#     print('it is not true')

# age=int('25')
# age=int(input("Enter your age:"))
# if age >= 17:
#     print('You are eligible')
# else:
#     diff = 17 - age
#     print(f'You will be eligible in {diff} years')

# age = int('25')
# age = (int(input("Enter your age:")))
# state = input("Enter your state:").upper()
states_17 = ['NY','CA','NC','VA','CT']
states_16 = ['NJ','WA','MA','TX','VT']
for i in range (3):
    age = (int(input("Enter your age:")))
    state = input("Enter your state:").upper()
    if age >= 16 and state in states_16:
        print('You are eligible:\n{states_16}')
        print("Avalable cars in these states:")
        for car in cars[:2]:
            print(f"\t{car}")
    elif age >= 17 and state in states_17:
        print('You are eligible:\n{states_17}')
        print("Avalable cars in these states:")
        for car in cars[2:]:
            print(f"\t{car}")
    else:
        #diff = 17 - age
        print(f'You are not eligible')
#

