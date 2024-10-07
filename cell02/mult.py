F_num = int(input("Enter the first number : "))
S_num = int(input("Enter the second number : "))
Mult = F_num * S_num

print(str(F_num) + "x" + str(S_num) + "=" + str(Mult))

if Mult > 0:
    print("The result is positive")
elif Mult < 0:
    print("The result is negative")
else :
    print("The result is positive and negative")
        
