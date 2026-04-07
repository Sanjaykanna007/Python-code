import pygame
import random
pygame.init()


screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Snake game")
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,35)
x=300
y=200
z=random.randint(0,580)
s=random.randint(0,380)
direction = "RIGHT" 
score = 0


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),(x,y,20,20))
    pygame.draw.rect(screen,(255,0,0),(z,s,20,20))
    pygame.display.update()
    clock.tick(60)            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    if keys[pygame.K_UP]:
        direction = "UP"
    if keys[pygame.K_DOWN]:
        direction = "DOWN"

    if direction == "RIGHT":
        x += 5
    if direction == "LEFT":
        x -= 5
    if direction == "UP":
        y -= 5
    if direction == "DOWN":
        y += 5
    if x<=0 or x>=600:
        running=False
    if y<=0 or y>=400:
        running=False
    if abs(x-z)<20 and abs(y-s)<20:
        score+=1
        z=random.randint(0,580)
        s=random.randint(0,380)
screen.fill((0,0,0))
text=font.render("Game over!  Score:  " + str(score),True,(255,0,0))
screen.blit(text,(150,180))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit
        
        
        


         
         
    
