print("hello world!")
# HOW TO FIND OUT THE ADDRESS OF THE ELEMENT
num=5
"every value holds an address"
print(id(num))
name="priyanka"
print(id(name))
# 'by using id ()function we can find out the  address '
a=19
b=a
print(a)
print(b)
print(id(a))
print(id(b))
# we are getting same adddress for both a and b
k=19
print(id(k))
a=9
print(id(a))
print(id(b))
# b is still getting the same address as a

# DATA TYPES:
# 1.NONE:when we won't assign any value to a variale then it will be none
# 2.NUMERIC:int,float,complex,boolean 
# int
num=5
print(num)
# float
num=2.5 
print(type(num))
# complex
num=6+1j
# complex basicall means a+ib but here we use "j"
# j is a square root of -1
print(type(num))
# Convert float value into intger value 
a=5.6
b=int(a)
print(type(b))
# Convert int value into float value 
k=19
k=float(b)
print(type(k))
# convert integer value into complex form
a=2
b=23
c=complex(a,b)
print(c)
print(type(c))
# BOOLEAN
# boolean is  a true or false
print(b<k)

# 3.list  
# 4.TUPLE
# 5.SET 
# 6.STRING
# 7.Range
# from 3 to 7 row is comes under sequence 
# list
li=[1,2,3,4]
print(type(li))
# tuple
tup=(1,2,3,4,5)
print(type(tup))
# set
s={1,2,3,4}
print(type(s))
# String
str="priynkaa"
print(type(str))
# Range:is a sequence of number
range(10)
# convert a range into a list
print(list(range(10)))

# 8.Dictionary
dict={
    "priynka":"samsung",
    "nikita":"iphone",
    "kajal":"oneplus"
}
print(dict)
# 9.fronzenset 

