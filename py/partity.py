# first_number = int(input("What's the number? "))

# if first_number % 2 == 0:
#      print(f"The {first_number} is Even")
# else:
#      print(f"The {first_number} is Odd")

def main():
     x = int(input("What's x? "))
     if isEven(x):
          print("Even")
     else:
          print("Odd")

def  isEven(n):
     # if n % 2 == 0:
     #      return True
     # else:
     #      return False


     return True if n  % 2 == 0 else False

# return  (n  % 2 == 0)

     
main()