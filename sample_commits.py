import random

words=['python','java','syntax','coding','programming']
turns=7
word= random.choice(words)
guesses= ''
a=[]
for i in word:
    a.append(i)
a=[*set(a)]

while turns>0:
    guess=input("Enter the letter: ")

    if guess in word:
        print("Correct! The letter ", guess,"is in the word. There is one or more letters in the word left.")
    else:
        turns-=1
        print("Incorrect! The letter", guess,"is not in the word. You have",turns,"turn(s) left to find the word.")

    guesses+=guess
    wrong=0
    c=0
    for b in guesses :
        if b in a:
            c=c+1
    if c== len(a):
        print("you won, contrats!! ")
        turns=0



    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print("_", end=' ')
            wrong+=1
    print(" \n")
else:
  print("u lost rip")
