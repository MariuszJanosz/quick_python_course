#string is surrounded with ' or "
s1="hergre"
s2='hrgdes'
print(s1)
print(s2)
#we can use ' and " inside string if they don't match string delimiters
s3="ger'weyges"
s4='qwfeg"dsfsgd'
print(s3)
print(s4)
#or by escaping them with \ 
s5="\"blah\""
print(s5)
#we can use ''' or """ to define multiline string
s6="""
this
is
a
multiline
string
"""
print(s6)
#we can access specific character in a string using []
#indexing starts at 0
s7="012345678"
print(s7[3])
#we can get part of string using slice syntax [n:m]
s8="0123456789"
print(s8[2:5])
#if we ommit n we would get slice starting from the beginning
#if we ommit m we would get slice that goes til the end of the string
print(s8[:5])
print(s8[2:])
#we can concatenate strings with + operator
s9="string1"
s10="string2"
print(s9 + " " + s10)
pi=3.14
print("PI = " + str(pi))
#here we can use format string instead it would automatically perform cast and concatenation
print(f"PI = {pi}")

