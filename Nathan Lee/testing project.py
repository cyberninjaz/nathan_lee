 stepI = int( input(" pick a number from 2-10 ") )
    JokeAnwserI = input(" Has your birthday already happened this year? ")
    stepII = int( input("What was the 5th year after you were born? (ex: born in 2000 so anwser is 2005)") )
if JokeAnwserI == "yes":
    print( str( ( ( ( (stepI * 2 + 5) * 50) + 1767) ) - (stepII - 5) + 1 ), "if there is a 3 digit number the last 2 digits is yor age if the number is 2 digit the last digit of the number is your age." ) 
elif JokeAnwserI == "no":
    print( str( ( ( (stepI * 2 + 5) * 50) + 1766 ) - (stepII - 5) + 2), " if there is a 3 digit number the last 2 digits is yor age if the number is 2 digit the last digit of the number is your age. ") 
else:
    print(" Your no fun. ")    
   