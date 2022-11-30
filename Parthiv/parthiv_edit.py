import random
print("\t \t \t MEAN YOUR WORDS!")
word_list=[["PINEY","PI","NEY","A mathematical expression/constant","The first 3 letters of a famous Brazilian footballer"],
           ["FANFARE","FAN","FARE","A supporter of someone/something","Money paid for the journey on a public transport"],
           ["PARKOUR","PARK","OUR","an open area in a town, often with grass or trees, where people can go to walk, play and so on","of or belonging to us"],
           ["LAPTOP","LAP","TOP","one journey around a running track","the highest part or point of something"]]
blank="_ "
a=random.choice(word_list)
length=len(a)
print("Rules:")
guess=""
c=a[0]
print("\t 1.You will be provided with meanings of various words which connect together to form one whole meanining full word")
print("\t 2.You can either guess the whole word, or you can guess one segment according to the hint given")
print("\t 3.You will have a total of 5 tries")
print("\t 4.Only full guess of each words are allowed. Partial guesses will be taken as wrong guess only")
print("Hints:")
print("\t Hint 1 is",a[3])
print("\t Hint 2 is",a[4])
o,p=0,0    
for i in range(5):
    if i==0:
        print("_ "*len(c))
    t=input("Enter your guess:")
    x=t.upper()
    y,s=slice(len(a[1])),slice(len(a[1]),len(a[0]))
    f=slice(0,len(a[2]))
    if (x[y]==a[1] and x[s]==a[2]):
        print("Congrats! You win! ",i+1,"number of guess(es)")
        break
    elif x[y]==a[1] and x[y] not in guess:
        print("Hint 1 correct but Hint 2 wrong")
        guess+=x[y]
        o=1
    elif (x[s]==a[2] or x[f]==a[2]) and (x[s] not in guess or x[f] not in guess):
        print("Hint 2 correct but Hint 1 is wrong")
        if x[s]==a[2] :
            guess+=x[s]
        else:
            guess+=x[f]
        p=1
    else:
        print("Your guess was wrong")
    if  o==1: 
        if p==1:
            for j in a[0]:
                print(j,end=" ")
            print()  
            print("Congrats! You win! ",i+1,"number of guess(es)")
            break
        else:
            for j in a[1]:
                print(j,end=" ")
            print(blank*len(a[2]))
    else:
        if p==1:
          print(blank*len(a[1]),end=" ")
          for j in a[2]:
                print(j,end=" ")
          print()
        else:
            print(blank*len(a[0]))
else:
    print("You Lost")
