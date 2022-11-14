import random
print("\t \t \t MEAN YOUR WORDS!")
word_list=["PINEY","FANFARE","PARKOUR","LAPTOP"]
random_word=random.choice(word_list)
blank="_ "
length=len(random_word)
print("Rules:")
print("1.You will be provided with meanings of various words which connect together to form one whole meanining full word")
print("2.You can either guess the whole word, or you can guess one segment according to the hint given")
print("3.You will have a total of 5 tries")
print("4.Only full guess of each words are allowed. Partial guesses will be taken as wrong guess only")
for i in range(5):
  print(blank*length)
  if(random_word=="PINEY"):
    print("Hint 1:A mathematical expression/constant")
    print("Hint 2:The first 3 letters of a famous Brazilian footballer")
    guess=int(input("Enter your guess:"))
    if(guess=="PI"):
      blank="PI"+blank*(length)-3
      #PLEASE EDIT THE BLANK PART, IDK HOW TO SWITCH UNDERSCORES TO TEXT
      print("Great, you've figured out the first hint")
    elif(guess=="NEY"):
      blank=
      #EDIT HERE
      print("Great, you've figured out the second hint")
    elif(guess=="PINEY"):
      print("Congrats!You've figured out the word!")
      break
    else:
      print("Wrong guess, try again")
  if(random_word=="FANFARE"):
    print("Hint 1:A supporter of someone/something")
    print("Hint 2:Money paid for the journey on a public transport")
    
    
      
      


