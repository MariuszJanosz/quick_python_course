#arithmetic operators
#addition
print(5 + 6)
#subtraction
print(5 - 6)
#multiplication
print(5 * 6)
#division
print(5 / 6)
print(6 / 6) #division always returns a float
#modulus
print(5 % 6)
#exponentiation
print(5 ** 6)
#floor division
print(5 // 6)
#assignment operators
#=
x=5
print(x)
#we can combine various operators with assignment to assign modified value to lhs
x<<=3
print(x)
#walrus operator := performs assignment and then uses assigned value in surrounding expression
if (count := 6) > 2:
    print(count) #here count was assigned 6 and this 6 was used in comparison > 2
#walrus operator has low precedence, so () are often needed
if count := 6 > 2:
    print(count) #here we first perform 6 > 2, the output of True is assigned to count and returned to be used by if
#ternary operator
var = 5 if 5 == 2 else 2
print(var)
#comparisons ==, !=, <, >, <=. >=
#can be chained like in math 1<x<3 is equivalent to 1<x and x<3
x=7
if 1<x<3:
    print(f"1<{x}<3")
else:
    print(f"x={x} does not satisfy 1<x<3")
#logical operators and, or, not
print(True and False)
#identity operators is, is not
#basically pointer to underlying object comparison under the hood
x=[]
y=[]
print(x is x)
print(x is y) #both x and y are empty lists, but they are different objects
x=3
y=3
print(x is y) #integer objects are singletons for each possible value, so since x=3 and y=3, we get x is y
#membership operators in, not in
print(5 in [1,2,3,4,5,6])
print(15 not in [1,2,3,4,5,6])
#bitwise operators &, |, ^, ~, <<, >>
print(3&5) #3=0b11, 5=0b101 => 3&5=0b011&0b101=0b001=1
#unary + and -
x=7
print(-x)
