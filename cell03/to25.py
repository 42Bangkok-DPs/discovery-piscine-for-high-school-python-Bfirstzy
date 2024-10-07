print("Enter a number less than 25")
I = int(input(" "))
if I <= 25:
    while I < 25:
        I +=1
        print("Inside the loop, my variable is"+ " " + str(I))
else:
    print("Error")
