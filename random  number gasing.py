import random 
a=random.randrange(1,4000)
user_input =int(input("enter your number:-"))

if user_input>a:
    print("your number is too high")
    print("computer number",a)
    
elif user_input<a:
    print("your number is too low")
    print("computer number",a)
    
else:
    print("your number is equal")
    print("computer number",a)        