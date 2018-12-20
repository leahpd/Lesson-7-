print('-'*65)
print ('100th Birthday Program:')
print()

print('Description: This program asks you for your current age and tells you the year that you will turn 100.')

age = input('What is your age today? ')
age = int(age)
yearsleft= 100 - age
yearsleft = int(yearsleft)
year = 2018 + yearsleft

print(year)
