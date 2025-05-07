#=================================Exercise 1: Variable Swap and Conditional Printings================================
# Python program to swap two variables

x=input("Enter value of x:")
y=input("Enter value of y:")

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#Implement a condition
if x>y:
  print("x is greater than y.")
elif x<y:
  print("x is less than y.")
elif x==y:
  print("x and y are equal.")
#=================================Exercise 2: Arithmetic Calculator================================
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

#============================================ EXERCICE 3 ============================================
def Celcius():
    Farenheit=float(input('Enter the temperature in Farenheit :'))
    Celcius=(Farenheit-32)/1.8
    print("The Temprerature in celcius is :", Celcius)

#def Farenheit():
#    Celcius=float(input('Enter the temperature in Celcius :'))
#    Farenheit=(Celcius*1.8)+32
#    print("The Temprerature in Farenheit is :", Farenheit)

def Kelvin():
    Celcius=float(input('Enter the temperature in Celcius :'))
    Kelvin=Celcius+273.15
    print("The Temprerature in Kelvin is :", Kelvin)

def main():
    print('''
          1. To convert in Celcius
          2. To convert into Kelvin
          3. Exit code''')
    choice=input("Inter the choice :")
    if choice=='1':
        Celcius()
    elif choice=='2':
        Kelvin()
    elif choice=='3':
        exit()
    else:
        print("It's an Invalid choice")
main()
#================================Exercise 4: Odd or Even Number Checker============================

num = int(input("Enter a number: "))
# Calculate the remainder when the number is divided by 2
mod = num % 2
# Check if the remainder is greater than 0, indicating an odd number
if mod==1:
    # Print a message indicating that the number is odd
    print("This is an odd number.")
elif mod==0:
    # Print a message indicating that the number is even
    print("This is an even number.")

#====================================== Exercise 5: Password Checker ========================
password = str(input("Enter a password: "))
bool=True
alphanumerique='abcdefghijklmnopqrstuvwxyz0123456789'
alphabet='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
if len(password) >= 8:
    for char in password:
        if (char in alphanumerique):
            continue
    print ("Strong Password.")

    #for char in password:
    #   if (char in alphabet):
    #        continue
    #    print("The password is not alphanumeric(including letters). Enter a new password")
        
    #for char in password:
    #    if (char in numbers):
    #        continue
    #    print("The password is not alphanumeric(including numbers). Enter a new password")
elif len(password) < 8:
    for char in password:
        if (char not in alphabet) or (char not in numbers):
            continue
    print("Weak Password.")