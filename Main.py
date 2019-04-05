import pygame
from pygame.locals import *

white = 255,255,255
blue = 0,0,200
HealthGray = 208,208,208
HealthYellow = 204,187,0
HealthRed = 238,0,0
black = 0,0,0
MessageYellow = 255,215,0

pygame.init()
screen = pygame.display.set_mode((1200,650))
pygame.display.set_caption("PUBG Pixel")

Main_Map = [0,0,0,0,0] * 2049
read = 0
try:
    outmap = open("Bin/Map/Forest.ini","r")
    for read in range(2048):
        line = outmap.readline()
        Main_Map[read] = line
    print("--------------------------------")
    print("    The Game Map : Forest ")
    print("        Load Sucessful")
    print("--------------------------------")
except:
    print("--------------------------------")
    print("   The Main Map Load Fatal !!!")
    print(" Error : File Lost : Forest.ini")
    print("       Error Code : -1")
    print("--------------------------------")
    exit()
try:
    Main_Image_People_WalkUp = pygame.image.load("Bin\Image\PeopleWalkUp.gif").convert_alpha()
    Main_Image_People_WalkLeft = pygame.image.load("Bin\Image\PeopleWalkLeft.gif").convert_alpha()
    Main_Image_People_WalkDown = pygame.image.load("Bin\Image\PeopleWalkDown.gif").convert_alpha()
    Main_Image_People_WalkRight = pygame.image.load("Bin\Image\PeopleWalkRight.gif").convert_alpha()
    Main_Image_Weapon_AKM = pygame.image.load("Bin\Image\AKM.gif").convert_alpha()
    Main_Image_Weapon_Mouse = pygame.image.load("Bin\Image\Mouse.PNG").convert_alpha()
    Main_Image_Weapon_Mouse_Shooting = pygame.image.load("Bin\Image\Mouse_Shooting.PNG").convert_alpha()
    Main_Image_Ground_Tree_0 = pygame.image.load("Bin\Image\Tree_0.PNG").convert_alpha()
    Main_Image_Ground_Tree_1 = pygame.image.load("Bin\Image\Tree_1.PNG").convert_alpha()
    Main_Image_Ground_Tree_2 = pygame.image.load("Bin\Image\Tree_2.PNG").convert_alpha()
except:
    print("--------------------------------")
    print(" The Image File Load Failed !!!")
    print(" Error : File Lost : Bin/Image")
    print("       Error Code : -2")
    print("--------------------------------")
    exit()
pygame.mouse.set_visible(False)
keying = False
shooting = False
myfont = pygame.font.Font("Bin\Fonts\simhei.ttf",25)
Main_Player_Mode = "Up"
Main_Player_Health = 100
Main_Player_Speed = 0
Main_Player_Speed2 = 3
Mouse_X = 0
Mouse_Y = 0

class Main_Message:
    def __init__(self,Message,Time,left):
        self.message = Message
        self.time = Time
        self.left = left
    def Print_Message(self):
        if(self.time > 0):
            self.mess_sur = myfont.render(self.message, True, MessageYellow)
            screen.blit(self.mess_sur,(600 - self.left,510))
            self.time -= 1
            return 1
        else:
            return 0
# Function
def Main_DrawMap():
    name , x , y , ex1 , ex2 = Main_Map[0].split()
    Main_Draw_Limit_Up = int(y) - 325
    Main_Draw_Limit_Down = int(y) + 325
    Main_Draw_Limit_Left = int(x) - 600
    Main_Draw_Limit_Right = int(x) + 600
    if(Main_Player_Mode == "Up"):
        screen.blit(Main_Image_People_WalkUp,(580,315))
    if(Main_Player_Mode == "Down"):
        screen.blit(Main_Image_People_WalkDown,(580,315))
    if(Main_Player_Mode == "Left"):
        screen.blit(Main_Image_People_WalkLeft,(580,315))
    if(Main_Player_Mode == "Right"):
        screen.blit(Main_Image_People_WalkRight,(580,315))
    vault = 0
    for vault in range(2048):
        name , x , y , ex1 , ex2 = Main_Map[vault].split()
        if(name == "FakeAK47"):
            if((int(x) >= Main_Draw_Limit_Left) and (int(x) <= Main_Draw_Limit_Right) and (int(y) >= Main_Draw_Limit_Up) and (int(y) <= Main_Draw_Limit_Down)):
                screen.blit(Main_Image_Weapon_AKM,(int(x) - Main_Draw_Limit_Left , int(y) - Main_Draw_Limit_Up))
        if(name == "Tree_0"):
            if((int(x) >= Main_Draw_Limit_Left) and (int(x) <= Main_Draw_Limit_Right) and (int(y) >= Main_Draw_Limit_Up) and (int(y) <= Main_Draw_Limit_Down)):
                screen.blit(Main_Image_Ground_Tree_0,(int(x) - Main_Draw_Limit_Left , int(y) - Main_Draw_Limit_Up))
        if(name == "Tree_1"):
            if((int(x) >= Main_Draw_Limit_Left) and (int(x) <= Main_Draw_Limit_Right) and (int(y) >= Main_Draw_Limit_Up) and (int(y) <= Main_Draw_Limit_Down)):
                screen.blit(Main_Image_Ground_Tree_1,(int(x) - Main_Draw_Limit_Left , int(y) - Main_Draw_Limit_Up))
        if(name == "Tree_2"):
            if((int(x) >= Main_Draw_Limit_Left) and (int(x) <= Main_Draw_Limit_Right) and (int(y) >= Main_Draw_Limit_Up) and (int(y) <= Main_Draw_Limit_Down)):
                screen.blit(Main_Image_Ground_Tree_2,(int(x) - Main_Draw_Limit_Left , int(y) - Main_Draw_Limit_Up))
    pygame.draw.rect(screen,black,(300,590,600,35),2)
    if(Main_Player_Health >= 60):
        pygame.draw.rect(screen,HealthGray,(302,592,Main_Player_Health*6-3,32),0)
    elif(Main_Player_Health >= 30):
        pygame.draw.rect(screen,HealthYellow,(302,592,Main_Player_Health*6-3,32),0)
    else:
        pygame.draw.rect(screen,HealthRed,(302,592,Main_Player_Health*6-3,32),0)
    if(shooting == False):
        screen.blit(Main_Image_Weapon_Mouse,(Mouse_X-15,Mouse_Y-15))
    else:
        screen.blit(Main_Image_Weapon_Mouse_Shooting,(Mouse_X-15,Mouse_Y-15))
                

Main_Message_Output = Main_Message(" " , 0 , 0)
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            textImage2 = myfont.render("KEYDOWN", True, blue)
            keying = True
        if event.type == KEYUP:
            textImage2 = myfont.render("KEYUP", True, blue)
            keying = False
        if event.type == MOUSEMOTION:
            textImage3 = myfont.render(str(event.pos),True , blue)
            Mouse_X , Mouse_Y = event.pos
        if event.type == MOUSEBUTTONDOWN:
            textImage4 = myfont.render("Player Shooting", True, blue)
            shooting = True
        if event.type == MOUSEBUTTONUP:
            textImage4 = myfont.render("Player Standing", True, blue)
            shooting = False
        pygame.key.set_repeat(10)
    if keys[K_ESCAPE]:
        exit()
    a = 65
    player , x , y , ex1 , ex2 = Main_Map[0].split()
    for a in range(127):
        if(Main_Player_Speed > Main_Player_Speed2):
             if(keys[a]):
                 b = chr(int(a))
                 if(b == "w"):
                     Main_Player_Mode = "Up"
                     Main_Map[0] = "Player " + x + " " + str(int(y)-6) + " " + ex1 + " " + ex2
                     Main_PLayer_Undo_X = x
                     Main_Player_Undo_Y = y
                     Main_Player_Speed = 0
                 if(b == "s"):
                     Main_Player_Mode = "Down"
                     Main_Map[0] = "Player " + x + " " + str(int(y)+6) + " " + ex1 + " " + ex2
                     Main_PLayer_Undo_X = x
                     Main_Player_Undo_Y = y
                     Main_Player_Speed = 0
                 if(b == "a"):
                     Main_Player_Mode = "Left"
                     Main_Map[0] = "Player " + str(int(x)-6) + " " + y + " " + ex1 + " " + ex2
                     Main_PLayer_Undo_X = x
                     Main_Player_Undo_Y = y
                     Main_Player_Speed = 0
                 if(b == "d"):
                     Main_Player_Mode = "Right"
                     Main_Map[0] = "Player " + str(int(x)+6) + " " + y + " " + ex1 + " " + ex2
                     Main_PLayer_Undo_X = x
                     Main_Player_Undo_Y = y
                     Main_Player_Speed = 0
                 if(b == "l"):
                     Main_Message_Output = Main_Message("你好吗，再您妈的见。" , 250 , 100)
                 if(b == "k"):
                     Main_Player_Health -= 1
                     if(Main_Player_Health <= 0):
                         Main_Message_Output = Main_Message("氪金成功" , 250,60)
                         Main_Player_Health = 100

    screen.fill(white)
    name , x , y , ex1 , ex2 = Main_Map[0].split()
    vault = 0
    for vault in range(2048):
        it_name , it_x , it_y , it_ex1 , it_ex2 = Main_Map[vault].split()
        if(it_name == "FakeAK47"):
            if((abs((int(it_x) - int(x))) < 30) and (abs(int(it_y) - int(y))) < 30):
                Main_Message_Output = Main_Message("氪金成功" , 5,60)
                Main_Player_Health -= 1
        if(it_name == "Tree_2"):
            if((abs(((int(it_x) + 40) - int(x))) < 30) and (abs((int(it_y) + 120) - int(y)) < 30)):
                Main_Map[0] = "Player " + Main_Player_Undo_X + " " + Main_Player_Undo_Y + " " + ex1 + " " + ex2
                Main_Message_Output = Main_Message(str(abs((int(it_y) + 30) - int(y))) + "--" + str(abs((int(it_x) - int(x)))), 5,60)
                Main_Player_Health -= 1
    Main_DrawMap()
    Main_Message_Output.Print_Message()
    Main_Player_Speed += 1
    pygame.display.update()
