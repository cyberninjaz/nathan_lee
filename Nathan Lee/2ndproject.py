import time

print(" Hello user welcome to the soul estimator. ")
Name = input(" What is your name? ")
print(" Hello, " + Name)
print("My name is Code error12, ok I'm going to begen the soul detecting. Anwser questions truthfully for a somewhat accurate anwser. If you want to goof with the system then you can anwser whatever way you want. No capitals please. ")
store = 0
Evil = False
questionI = input("Question 1: Do you offten hold doors open for others? Don't anwser with any capitals. ")
if questionI == "yes":
    store = store + 1
elif questionI == "no": 
    store = -1
questionII = input('Question 2: Out of these 5 colors what is your favorite? purple, yellow, blue, red, or pink? ')
questionIII = input("Question 3: Are you afraid of insects?(Do you not like bugs?) ")
print(" These are the Last 2 question for soul type when we move on to traits. ")
questionIV = input("Question 4: Do you use jokes often? ")
questionV = input(" Do you like sports ")
if questionV == "yes":
    mini = input("Do you play in a league? ")
    store = store -1

elif questionV == 'no':
    store = store + 1    
joke = False
if questionII == 'blue' and store == 1 and questionIII == 'yes'  and questionIV == "no":
    print("Your soul type is mixed, shy but kind")
elif questionII == "purple" and store == 1 and questionIII == "yes" and questionIV == "no":
     print("Your soul type is mixed, shy but kind")
elif questionII == 'purple' and store == -1 and questionIII == "yes" and questionIV == "no":     
    print('your estimated soul type is shy however there is a possibility it is mean but that chace is small.')
elif questionII == 'purple' and store == -1 and questionIII == "no"  and questionIV == "no":     
    print('your estimated soul type is shy however there is a possibility it is mean but that chace is small.')    
elif  questionII == 'blue' and store == 1 and questionIII == "no"  and questionIV == "no":     
    print('your estimated soul type is shy however there is a possibility it is mean but that chace is small.')    
elif  questionII == 'blue' and store == -1 and questionIII == "yes" and questionIV == "no":     
    print('your estimated soul type is shy however there is a possibility it is mean but that chace is small.')        
elif  questionII == 'red' and store == -1 and questionIII == 'yes' or questionIII == 'no'  and questionIV == "no":      
    print("your soul type is evil.")
    Evil = True
elif  questionII == 'red' and store == -1 and questionIII == 'yes'  and questionIV == "no":      
    print("your soul type is evil.")
    Evil = True
elif  questionII == 'red' and store == -1 and questionIII == 'yes' and questionIV == "yes":      
    print("your soul type is evil.")  
    Evil = True
    joke = True
elif  questionII == 'red' and store == -1 and questionIII == 'no' and questionIV == "yes":      
    print("your soul type is evil.")     
    ioke = True
elif questionII == 'yellow' and store == 1 and questionIII == 'no'  and questionIV == "yes":  
    print("You are kind and silly.")   
    joke = True
elif questionII == 'pink' and store == 1:
    print("You are kind")
    joke = True
elif questionII == "pink" and questionIII == "no": 
    print("You are somewhat kind.")
    Joke = True
elif questionII == "yellow" and store == 1:
    print("you are nice")
    joke = True
elif questionII == "red" and store == 1:
    print("You are decently nice but not too nice.")
elif questionII == "yellow" and store == -1 and questionIV == no:
    print("You are mysterious")   
elif store == 1:
    print("you are somewhat kind.")
    joke = True
elif store == -1:
    print("you are not too nice.")
elif store == -2:
    print(" Your soul is aggresive and fame hungry. ")    
elif questionII == 'red' and questionIV == 'yes' and store == 1:
    print('you are pretty nice')    
    joke = True
elif store == 2:
    print(" You are nice and helpful. ")  
    joke = True  
elif store == 0:
    print(" You are nice when you are happy but when mad your soul becomes aggresive")
    joke = True    
elif questionII == 'red' and questioniv == 'yes' and store == -1:    
    print("your soul is twisted in booth good and bad")
    joke = True
else:
    print(" i dont understand")     
if Evil == True:
    print('oof')
if joke == True:
    funny = input(" Wanna hear a joke? ")
    if funny == "yes" or funny == "sure":
        stepI = int( input(" pick a number from 2-10 ") )
        JokeAnwserI = input(" Has your birthday already happened this year? ")
        stepII = int( input("What was the 5th year after you were born? (ex: born in 2000 so anwser is 2005) ") )
        if JokeAnwserI == "yes":
            print( str( ( ( ( (stepI * 2 + 5) * 50) + 1767) ) - (stepII - 5) + 1 ), "if there is a 3 digit number the last 2 digits is yor age if the number is 2 digit the last digit of the number is your age." ) 
        elif JokeAnwserI == "no":
            print( str( ( ( (stepI * 2 + 5) * 50) + 1766 ) - (stepII - 5) + 2), " if there is a 3 digit number the last 2 digits is yor age if the number is 2 digit the last digit of the number is your age. ") 
    else:
            print(" Your no fun. ")    

time.sleep(3)

if Name == "Piankhi" or Name == "piankhi":
    print(" Piankhi bad, your face. Piankhi 是 大 便 :D")

print("              ")
print("Did you like the game/detector? choose a letter. I skipped f because reasons. ")
like = input("a:yes b:no c:very d: what's the point? e:Piankhi bad g:Piankhi good      your anwser:")
if like == "a" or like == 'c':
    print("yay! Thank-you")
elif like == "b":
    sure = input(" are you sure? ") 
    if sure == 'yes':
        sureI = input(" fine then ill delete your fortnite account and if you dont have one then REEE.") 
    elif sure == 'no':
        print("yay!")
    else:
        print("?")    
elif like == "e":
    print("True that")
elif like == 'g' and Name == "Piankhi" or Name == "piankhi":
    print("well thats just because your Piankhi zimmerman. everyday more lies. Piankhi不好  :D")
elif like == 'g':
    print(" Everyday more lies. Piankhi不好 :D")    
elif like == 'd':
    print(" I dont know, wasting your time I guees. ")        
time.sleep(2)

print(' Visionist and Developer: Nathan Lee ')

time.sleep(2)

print(' Overveiwed/tested by: Jake, Alex, Piankhi Zimmerman')

time.sleep(2)

print(" Special thanks to Christopher D'Angelo")

time.sleep(2)

print("Hey there want to see more games made by me?")
print("If so check out these links :D (Please note that I made these games more than 2 years ago and that they will most likely not be updated. Expect bugs and glicthes)")
print("http://www.cyberninjaz.com/projects/student.php?pid=galaxydefender2")
print("http://www.cyberninjaz.com/projects/student.php?pid=galaxydefender")




 




