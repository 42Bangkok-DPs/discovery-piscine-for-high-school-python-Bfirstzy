import sys

if len(sys.argv) != 2:
    print("none")
else:
    ask = input("What was the parameter? ")

    if ask == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
