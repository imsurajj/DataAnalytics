#data types (int,float,str,etc)
a=5
b=4.3
c='Suraj'
d=False
print('The type is',(type(a)))
print('The type is',(type(b)))
print('The type is',(type(c)))
print('The type is',(type(d)))

#Type conversion
a=5
b=4.3
c="42"
print(type(float(a)))    #conversion of int to float type
print(type(str(b)))     #conversion of float to str type
print(type(int(c)))     #conversion of str to int type

#Operators (5 types)
#Arithmetic (+,-,*,**,/,//,%)
a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
print("\nArithmetic Operators: ")
print("Addition: ", a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ", a/b)
print("Floor division: ",a//b)
print("Modulus: ",a%b)
print("Exponent: ",a**b)

#Comparison
print("\nComparison operators: ")
print("a==b: ",a==b)
print("a!=b: ",a!=b)
print("a>b: ",a>b)
print("a<b: ",a<b)
print("a<=b: ",a<=b)
print("a>=b: ",a>=b)

#logical
x=True
y=False
print("\nLogical Operators: ")
print("x and y: ",x and y)
print("x or y: ",x or y)
print("not x:", not x)

#membership
my_list=[40,30,60,10,20]
print("\nMembership operator: ")
print("10 in my_list: ",10 in my_list)
print("50 not in my_list: ",50 not in my_list)

#identity operators
x=100
y=500
z=100
print("\nIdentity operator: ")
print("x is y: ",x is y)
print("z is not y: ", z is not y)