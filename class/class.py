class v3:
    string = "3D vector"
    __private = 5

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.__loc_pr = 6


    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"
    

    def get_length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    

    def scalar_product(self, other):
        if type(other) is not v3:
            raise TypeError
        return self.x*other.x + self.y*other.y + self.z*other.z


    def vector_product(self, other):
        if type(other) is not v3:
            raise TypeError
        return v3(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)


    def get_pr():
        return v3.__private

    def get_loc_pr(self):
        return self.__loc_pr

vec1 = v3(1,2,3)
print(vec1)
print(vec1.get_length())
vec2 = v3(1,2,3)
print(vec1.scalar_product(vec2))
try:
    print(vec1.scalar_product(6))
except TypeError:
    print("Incorrect type")
print(v3(7,1,9).vector_product(v3(1,-6,2)))

#class properties are shared by all objects
print(vec1.string)
print(vec2.string)
v3.string = "New string"
print(vec1.string)
print(vec2.string)
#but if we add property with the same name to object it would shadow shared version
vec1.string = "trhfdgsf"
print(vec1.string)
print(vec2.string)
#variables prefixed with __ are private
#we can access them only from the inside of the class
print(v3.get_pr())
try:
    print(v3.__private)
except:
    print("It's private")
print(vec1.get_loc_pr())
try:
    print(vec1.__loc_pr)
except:
    print("It's private")
#methods can also be made private with __
#private method can b used only inside the class
#in reality private methods, and variables are a lie
#python simply mangles their names by prefixing with _classname
print(v3._v3__private) #it works fine

