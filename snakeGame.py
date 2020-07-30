import pygame
import random
import os
x=pygame.init()
pygame.mixer.init()

#colors list
white=(255,255,255)
red=(255,0,0)
black=(0,0,0) 
snakegreen=(35,45,40)
#Creating window
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
#Images
welcome_img=pygame.image.load("image/welcome.jpg")
welcome_img=pygame.transform.scale(welcome_img,(screen_width,screen_height)).convert_alpha()
bgimg=pygame.image.load("image/bg.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
gameOver=pygame.image.load("image/game_over3.png")
gameOver=pygame.transform.scale(gameOver,(200,200))
snake_img=pygame.image.load("image/snake6.png")
snake_img=pygame.transform.scale(snake_img,(200,200))
python_img=pygame.image.load("image/py5.png")
python_img=pygame.transform.scale(python_img,(150,150))
final_img=pygame.image.load("image/bc.png")
final_img=pygame.transform.scale(final_img,(screen_width,screen_height)).convert_alpha()
pygame.display.update()
clock=pygame.time.Clock()

pygame.display.set_caption("SnakesWithAshu")
font=pygame.font.SysFont("comicsansms",35)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,(x,y))
def plot_snake(gameWindow,black,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False
    pygame.mixer.music.load("sound/bg1.mp3")
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.blit(welcome_img,(0,0))
        text_screen("Press SPACE BAR to Continue this Game",red,115,1)
        text_screen("Developer-AshviniSharma",(255,242,128),470,550)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)        
        
#game Loop
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=20
    fps=60
    velocity_x=0
    velocity_y=0
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    score=0
    init_velocity=5
    snk_list=[]
    snk_length=1
    #Check if high score file exists...
    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt","w") as w:
            w.write("0")
    with open('highScore.txt','r') as r:
        high_score=r.read()
    while not exit_game:
        if game_over:
            with open("highScore.txt",'w') as w:
                w.write(str(high_score))
            gameWindow.blit(final_img,(0,0))
            gameWindow.blit(gameOver,(350,60))
            gameWindow.blit(python_img,(650,80))
            gameWindow.blit(snake_img,(90,60))
            text_screen("Press ENTER to continue",snakegreen,260,290)
            text_screen("Your score:"+str(score),snakegreen,330,330)
            if score<=160:
                text_screen("Not good performance, Try again!",snakegreen,170,375)
            elif score>100:
                text_screen("Carry on,You can achive good score",snakegreen,160,375)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                pygame.mixer.music.load("sound/run.mp3")
                pygame.mixer.music.play()
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    if event.key==pygame.K_q:
                        score+=10
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y    
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                pygame.mixer.music.load("sound/snakehit.mp3")
                pygame.mixer.music.play()
                score+=8
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(high_score):
                    high_score=score
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score)+"  High Score: "+str(high_score),(255,51,51),5,-5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("sound/oh-shit.mp3")
                pygame.mixer.music.play()
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("sound/oh-shit.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()