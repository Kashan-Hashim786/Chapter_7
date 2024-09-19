sum = 0
number = int(input("Enter a number : "))
i = 1
if number==0 or number<0:
        print(f"The number {number} is not valid")
        number = int(input("Enter a valid number : "))
        while i<=number:
          sum = sum + i
          i += 1
      

print(f"Sum of number from 1 to {number} : {sum}")
