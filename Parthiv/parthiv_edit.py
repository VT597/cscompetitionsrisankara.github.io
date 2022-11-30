import random
print("\t \t \t MEAN YOUR WORDS!")
word_list=[["PINEY","PI","NEY","A mathematical expression/constant","The first 3 letters of a famous Brazilian footballer"],
           ["FANFARE","FAN","FARE","A supporter of someone/something","Money paid for the journey on a public transport"],
           ["PARKOUR","PARK","OUR","an open area in a town, often with grass or trees, where people can go to walk, play and so on","of or belonging to us"],
           ["LAPTOP","LAP","TOP","one journey around a running track","the highest part or point of something"]]
blank="_"
a=random.choice(word_list)
length=len(a)
print("Rules:")

c=a[0]
print(a)
print("\t 1.You will be provided with meanings of various words which connect together to form one whole meanining full word")
print("\t 2.You can either guess the whole word, or you can guess one segment according to the hint given")
print("\t 3.You will have a total of 5 tries")
print("\t 4.Only full guess of each words are allowed. Partial guesses will be taken as wrong guess only")
print("Hints:")
print("\t Hint 1 is",a[3])
print("\t Hint 2 is",a[4])
    
for i in range(5):
    if i==0:
        print("_"*len(c))
        
    t=input("Enter your guess:")
    x=t.upper()
    y,s=slice(len(a[1])),slice(len(a[1]),len(a[0]))
    f=slice(len(a[1])-len(a[0]))
    print(x[y])
    print(x[s])
    
    if x[y]==a[1] and x[s]==a[2]:
        print("you win ")
        break
    elif x[y]==a[1]:
        print(a[1],blank*(len(a[2])))    
    elif x[s]==a[2] or x[y]==a[2]:
        print(blank*(len(a[1])),a[2])
