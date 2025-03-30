#Program By Leo Johnson in 2025
#Program Version 1.0
print("Loading...")
score = 0

print("The Test by Leo Johnson - Program version 1.1")
print("Welcome To The Test!")
name = input("What's your name? ")
print("Ok "+name+", are you ready (Too bad coz we are starting now.)")

q1 = input("Alright! Question 1. You have a bottle of coke and you have mentos. Do you put the mentos in the coke? (y/n) ")
if q1 == "y":
    score = score - 1
if q1 == "n":
    score = score + 1
    
q2 = input("Question 2. You are on the bus. Someone has fallen asleep and leaned on you (You don't know them) Do you push them off? (y/n) ")
if q2 == "y":
    score = score - 2
if q2 == "n":
    score = score + 3
    
q3 = input("Alright " + name + ". Question 3. Your friends computer is open do you 1: Install a virus 2: Search Their browser history 3: Delete Their Stuff 4: Do Nothing (1/2/3/4) ")
if q3 == "1":
    score = score - 5
if q3 == "2":
    score = score - 1
if q3 == "3":
    score = score - 4
if q3 == "4":
    score = score + 3

if score == 7:
    print(name + "! You're doing amazing!")
    
q4 = input("What is rizz? (Awnser in one word all lowercase) ")
if q4 == "charisma":
    score = score + 2
else:
    score = score + 1

q5 = input("You fart in the car, do you 1: own up 2: blame the dog? (1/2) ")
if q5 == "1":
    score = score + 5
if q5 == "2":
    score = score - 5

q6 = input("Do you wear clean underwear everyday? (y/n) ")
if q6 == "y":
    score = score + 2
if q6 == "n":
    score = score - 1000
    
q7 = input("You find a wallet in the park. Do you 1: Spend big 2: Hand it in to the police 3: Purcahse presents for the family (1/2/3) ")
if q7 == "1":
    score = score - 10
if q7 == "3":
    score = score - 3
if q7 == "2":
    score = score + 5
    
q8 = input("Your mums not home and you find her secret stash of chocholate. Do you 1: Wait until shes home and ask to have some 2: Help yourself? (1/2)  ")
if q8== "1":
    score == score + 5
if q8 == "2":
    score == score - 4
    
q9 = input("Pretend your best friend has a serious phobia of spiders. On your next sleepover with them do you put your fake spider in their bed as a joke (y/n) ")
if q9 == "y":
    score = score - 7
if q9 == "n":
    score = score + 4
    
q10 = input("Is your password 'password' or '1234'? (y/n) ")

rs = "n"
if score > -998 and score < 0:
    rs = "f"
if score < -999:
    rs = "uf"
if score > 0:
    rs = "p"

print("Loading & Saving Score...")
score = str(score)
scorefile = open(name+"'s score_file.txt","w")

if rs == "f":
    scorefile.write(name+"'s score is: "+score+". They Failed\nQuestion 1 answer: "+q1+"\nQuestion 2 answer: "+q2+"\nQuestion 3 answer: "+q3+"\nQuestion 4 answer: "+q4+
    "\nQuestion 5 answer: "+q5+"\nQuestion 6 answer: "+q6+"\nQuestion 7 answer: "+q7+"\nQuestion 8 answer: "+q8+"\nQuestion 9 answer: "+q9+"\nQuestion 10 Awnser: "+q10)
if rs == "p":
    scorefile.write(name+"'s score is: "+score+". They Passed\nQuestion 1 answer: "+q1+"\nQuestion 2 answer: "+q2+"\nQuestion 3 answer: "+q3+"\nQuestion 4 answer: "+q4+
    "\nQuestion 5 answer: "+q5+"\nQuestion 6 answer: "+q6+"\nQuestion 7 answer: "+q7+"\nQuestion 8 answer: "+q8+"\nQuestion 9 answer: "+q9+"\nQuestion 10 Awnser: "+q10)
if rs == "uf":
    scorefile.write(name+"'s score is: "+score+". They Failed & don't wear clean undies\nQuestion 1 answer: "+q1+"\nQuestion 2 answer: "+q2+"\nQuestion 3 answer: "+q3+"\nQuestion 4 answer: "+q4+
    "\nQuestion 5 answer: "+q5+"\nQuestion 6 answer: "+q6+"\nQuestion 7 answer: "+q7+"\nQuestion 8 answer: "+q8+"\nQuestion 9 answer: "+q9+"\nQuestion 10 Awnser: "+q10)
scorefile.close()


if rs == "f":
    print("Your score is: "+score+". You failed.")
if rs == "uf":
    print("Try wearing clean undies next time "+name+".")
if rs == "p":
    print("Your score is: "+score+". Great job "+name+", you passed!")
print("Thanks for playing the test! Your results have been saved as: "+name+"'s score_file.txt")
