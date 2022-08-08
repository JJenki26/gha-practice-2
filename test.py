import sys


try:
    print(sys.argv[1] + " is " + sys.argv[2] + "-years old.")
except:
    usrName = input("Please enter your name: ")
    usrAge = input("Please enter your age: ")
    print(usrName + " is " + usrAge + "-years old.")