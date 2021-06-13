name = input('What is your Name? ')
print('Nice to meet you', name)

from pandas import read_csv
mydf = read_csv('mycsv.csv')
print(mydf.head())

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())

for _ in range(10):
  print(fake.name())
