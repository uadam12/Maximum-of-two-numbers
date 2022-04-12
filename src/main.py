print ("Welcome to maximum of two numbers calculator")

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))


def max(a, b):
  return a if a > b else b


print ("The maximum of {} and {} = {}".format(num1, num2, max(num1, num2)))

print ("Bye")