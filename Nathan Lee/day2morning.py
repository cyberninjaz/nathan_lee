number = input("choose a pyrimid height. ")
number = int(number)
for i in range(1,1+number):
    print( "#" * (number - i +1) )