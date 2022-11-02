import pygame, sys
from pygame.locals import *
import time
import random

# set up the window
screen = pygame.display.set_mode((1080 , 1080), 0, 32)
pygame.display.set_caption('Hangman Game')

rand_word=["apple","banana","orange"]
file=open("Random words.txt","r")
MAGENTA=(255, 255, 255)
YELLOW=(0,   0, 255)
X = 400
Y = 400

pygame.init()
# Run until the user asks to quit
running = True
screen.fill(MAGENTA)
q=0
y=300
lword=[]
l=len(rand_word)
for o in range(l):
    lword.append("")
r=list(rand_word)
print(r)



# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()

# Draw a solid blue circle in the center
pygame.draw.circle(screen, YELLOW, (540, 525), 525)

used_words=[]
heart=9

while running:
    try:
        # Fill the background with white
        
        if heart<=8:
            pygame.draw.rect(screen,CYAN,(250,580,300,30))
        if heart<=7:
            pygame.draw.rect(screen,CYAN,(385,200,35,400))
        if heart<=6:
            pygame.draw.rect(screen,CYAN,(400,200,300,30))
        if heart<=5:
            pygame.draw.rect(screen,CYAN,(650,200,15,150))
        if heart<=4:
            pygame.draw.circle(screen, CYAN, (658, 360), 40)
        if heart<=3:
            pygame.draw.rect(screen,CYAN,(655,400,10,150))
        if heart<=2:
            pygame.draw.rect(screen,CYAN,(560,450,200,10))
            
        if heart<=1:
            pygame.draw.polygon(screen, CYAN, [(650, 540), (658, 548), (608, 608), (600, 600)])
            pygame.draw.polygon(screen, CYAN, [(666, 540), (658, 548), (700, 600), (710, 600)])
            
        if heart==0:
            a=1
            for i in range(100):
                font2 = pygame.font.SysFont("Game Over", 110)
                img2 = font2.render("Game Over", True, GREEN)
                screen.blit(img2, (450, a))
                screen.blit(img2, (0, a))
                screen.blit(img2, (900, a))
                pygame.display.update()
                time.sleep(0.03)
                a+=50
            break
            
        if lword==r:
            font2 = pygame.font.SysFont("Well Done!", 150)
            img2 = font2.render("Well Done!", True, GREEN)
            screen.blit(img2, (270, 650))
            time.sleep(3)
            import First_Game.py
        
        
        
        x=300
        
        for i in range (len(rand_word)):
            pygame.draw.rect(screen,CYAN,(x,850,30,10))
            x+=50
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if  event.type==KEYDOWN:   
                
                if event.key == K_ESCAPE:
                        running = False
                    
                if chr(event.key) in used_words:
                    print("Letter already Used")
                    
                else:
                    used_words.append(chr(event.key))
                    if chr(event.key) in rand_word:
                        for m in range(rand_word.count(chr(event.key))):
                            sysfont = pygame.font.get_default_font()
                            
                            
                            font1 = pygame.font.SysFont(chr(event.key), 72)
                            img1 = font1.render(chr(event.key), True, GREEN)
                            
                            ind=rand_word.index(chr(event.key))
                            rand_word_list=list(rand_word)
                            rand_word_list[ind]=" "
                            rand_word=""
                            lword[ind]=chr(event.key)
                            print(lword)
                            
                            for i in rand_word_list:
                                rand_word+=i
                            
                            screen.blit(img1, (y+(50*ind), 800))
                            pygame.display.update()
                    else:
                        l=ord(chr(event.key))-96
                        sysfont = pygame.font.get_default_font()
                        
                        
                        
                        font1 = pygame.font.SysFont(chr(event.key), 40)
                        img1 = font1.render(chr(event.key), True, BLUE)
                        
                        if l>6 and l<13:
                            q=50
                        elif l>12 and l<19:
                            q=100
                        elif l>=18 and l<25:
                            q=150
                        elif l>=24 and l<27:
                            q=200
                        else:
                            q=0
                        if l%6!=0:
                            l=l%6
                        if l==12:
                            l=6
                        if l==18:
                            l=6
                        if l==24:
                            l=6
                        
                        
                        screen.blit(img1, (50*l, 350+q))
                        
                        pygame.display.update()
                        l+=1
                        heart-=1
                    
                        
        
        pygame.display.flip()
        pygame.display.update()
    except:
        pass

# Done! Time to quit.
pygame.quit()
    
