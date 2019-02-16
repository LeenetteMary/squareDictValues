year = int(input('Enter year of birth:'))

age = 2019 - year

if age  < 18:
    print('You are a minor')

elif age > 18 and age < 36:
    print('You are an adult')

else:
    print('You are an elder')