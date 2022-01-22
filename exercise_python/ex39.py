# create a mapping of state to abbreviation
#不要忘记 ":"和 ","
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan abbreviation is: ",states['Michigan'])
print("Florida abbreviation is: ",states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
#list(cities.items()返回一个class 'list'
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
#states.items()返回一个class 'dict_items'
for state, abbrev in (states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")

#清理字典中所有元素
a = states.clear()
print(a)

#返回字典中的value
b = cities.values()
print(type(b))
print(b)

#返回字典中的key
c = cities.keys()
print(type(c))
print(c)