n=int(input("Enter a number: ")) #Taking input from the user
a=0
b=1

if n==0:
    print("Number cannot be zero") #for checking if the number is 0
    
elif n<0:
    print("Number cannot be negative") #for checking if the number is Negative
    
else:
    print(a)
    print(b)
  
    for i in range(n):
        a,b=b,a+b
        print(b)
    

