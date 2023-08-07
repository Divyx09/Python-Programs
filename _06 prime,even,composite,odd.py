num = int(input("Enter a number: "))
number = False
if num > 1:
    
    for i in range(2,num):
        if (num % i) == 0:
           
            number = True
            
            break
if number:
    print(num, "is a composite number")
else:
    print(num, "is a prime number")


if(num%2==0):
    print(num,"is a even number")
else:
    print(num,"is a odd number")