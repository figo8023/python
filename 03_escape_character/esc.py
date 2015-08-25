print('I\'m learning\nPython.')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print('''line1\\
line2
line3''')
print(r'''line1\\
line2
line3''')
print(3>2)
print(5>3 or 1>3)
print(5>3 and 1>3)
age = int(input('Please enter the age: '))
if age >=18:
	print('adult')
else:
	print('teenager')
a = 'ABC'
b = a
a = 'XYZ'
print(b)
x= 10/3
y= 10//3
z= 10%3
print(x,y,z)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)
