#function syntax
#def name(parameters):
#    body
def my_func1():
    print("Hello world!")
#we can return value from a function with return
def my_func2():
    return 0
#if we don't use return it would return None
#functions can take arguments
def my_func3(arg1, arg2):
    print(arg1, arg2)
#number of arguments passed has to match number of parameters specified in definition
#we can make some arguments to have default values
#if some argument has default value, all arguments to the right also have to have default values
#we can call such function with less arguments, the unspecified arguments would take default values
def my_func4(arg1, arg2, arg3="htrgefw", arg4="xxx"):
    print(arg1, arg2, arg3, arg4)
#adding ,/ after the list of parameters makes it that the function would accept only positional arguments
def my_func5(arg1, arg2, /):
    print(arg1, arg2)
#adding *, before the list of parameters makes it that the function would accept only kwargs
def my_func6(*, arg1, arg2):
    print(arg1, arg2)
#in general all arguments before / have to be positional, and all after * have to be kwargs
def my_func7(arg1, /, *, arg2):
    print(arg1, arg2)
#if we prefix a parameter name with * it would accept more arguments packed into a tuple
#*-prefixed parameter has to come after all regular parameters
def my_func8(*args):
    for x in args:
        print(x)
#if we prefix a parameter name with ** it would accept more kwargs packed into a dictionary with parameter names as keys
#**-prefixed parameter has to come after all regular parameters
def my_func9(**kwargs):
    print(kwargs["a"])
#if we want to use regular, *-prefixed, and **-prefixed parameters in one function they have to come in this order
#positional arguments would be assigned to regular parameters,
#remaining positional arguments would be assigned to *-prefixed parameter as a tuple
#remaining kwargs would be assigned to **-prefixed parameter as a dictionary
def my_func10(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
#functions in python are objects and can be returned from function as any other object
#using this we can create decorators, i.e., functions that modify other functions
def decorator_example(func):
    def ret_func(arg):
        return func(arg).upper()
    return ret_func
@decorator_example
def get_string(string):
    return "string: " + str(string)
#it is usefull for example for timing
#def timer_decorator(func):
#   start = get_time()
#   x = func()
#   time_ellapsed = get_time() - start
#   return (x, time_ellapsed)
###################################
my_func1()
print(my_func2())
print(my_func1())
my_func3(1, "kjedyhgou")
try:
    my_func3(1,2,3)
except:
    print("Incorrect number of arguments")
my_func4(1,2)
#if we specify parameter name at call site with arg_name=value, we can change order
my_func4(arg1=2,arg2=1)
#if we want to mix positional and kwargs, kwargs have to come after positional ones
my_func4(1, arg3=6, arg2=3)
my_func5(1,2)
try:
    my_func5(arg2=1,arg1=2)
except:
    print("This function does not accept kwargs")
my_func6(arg1=1, arg2=2)
try:
    my_func6(1,2)
except:
    print("This function accepts only kwargs")
my_func7(1, arg2 = 2)
my_func8(1,2,3,4,5,6)
my_func9(a=2,b=4)
my_func10(1,2,3,a=4)
my_func10(1,2,a=3)
my_func10(1,2,3)
my_func10(1,2)
try:
    my_func10(1)
except:
    print("Requires at leas 2 positional arguments")
#we can use * and ** in function calls to unpack list and dictionaries into arguments and kwargs respectively
my_func10(*[1,2],**{"a":15})
print(get_string("hrftngdg"))

