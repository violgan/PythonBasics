student1 = {'name': 'Hamza', 'gpa' : 3.8, 'lastName': 'Hamrakulov'}
student2 = {'name': 'Alexa', 'gpa' : 3.9, 'lastName' : 'Moiseeva'}
print(student1['name'], student1['gpa'])

print('###################################')

for key in sorted(student1):
    print('key is:', key)
for key in student1.keys():
    print('key is:', key)
print('###################################')

for key in student1.keys():
    print('value is', student1[key])
print('###################################')

for value in student1.values():
    print('value is', value)
print('###################################')
for dkey, dvalue in student1.items():
    print('key is', dkey)
    print('value is', dvalue)

print("##########Nesting dictionaries###########")
dclass_2020 = {'student1' : student1, 'student2' : student2}
print(dclass_2020)
for key, value in dclass_2020.items():
    print('Key of the element:', key)
    print('Value of the element:', value)
    print('Name of the student:', value['name'])
    print('GPA of the student:', value['gpa'])
    print('Last Name of the student:', value['lastName'])
    print("____________________")


####### 6-5 ######

rivers = {'nile': 'egypt', 'hudson':'usa', 'volga':'russia', 'mississippi' : 'usa', 'thames':'uk'}

for river, country in rivers.items():
    if country in ['usa', 'uk']:
        print(f"The {river.title()} runs through {country.upper()}")
    else:
        print(f"The {river.title()} runs through {country.title()}")


#####Use a loop to print the name of each river included in the dictionary .
print('Rivers are: ')
for river in rivers.keys():
    print('\t', river.title())

### Use a loop to print the name of each country included in the dictionary .
print('Countries are:')
for country in sorted (rivers.values(), reverse=True):
    if country in ['usa', 'uk']:
        print('\t', country.upper())
    else:
        print('\t', country.title())


########### 6-11 ###########
cities = {'new york': {'country': 'USA', 'population': 8.2,'fact': 'Big Apple'},
          'istanbul': {'country':'turkey', 'population':15.52, 'fact':'Constantinople'},
          'tashkent':{'country': 'uzbekistan', 'population':2.5, 'fact' : 'Stone city'},
          'moscow': {'country' : 'russia', 'population' : 12.53, 'fact' : 'Kremlin'} }

##city is very beautifull city in country. It has population population and also called as fact
for city, info in cities.items():
    print(city)
    print(info)
    print(f"{city.title()} is very beautifull city in {info['country'].title()}."
          f"It has {info['population']} mln population and also called as {info ['fact']}.")
