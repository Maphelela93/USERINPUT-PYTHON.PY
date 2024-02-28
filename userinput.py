name = input("Enter your name:")
age = int(input("Enter your age:"))
location = input("Enter your location:")

# first approach
print("hello" , name, "you are", age, "year old and live in", location)

#seond aproach %
print ("second approach")
print ("hello %s you are %d years old and live in %s"%(name, age, location))

#third approach format
print ("third approach")
print ("hello {} you are {} years old and live in{}".format (name, age, location))