'''
This is rockman game
developed by T.S Chandrakasem University
dept. Computer Science and A.I.
use in OOP class 1/2024
'''

import pygame


class Rockman:
    def __init__(self):   #constructor -> สร้าง object ครั้งแรก
       self.x = 65
       self.y = 533
       self.dir = 1    #0-> left, 1->right
       self.is_jump = False
       self.jump_loop_count = 0
       self.is_move = False

    def move(self,dir):
        if dir == 0:   #left
            self.x -= 10
        elif dir == 1:   #right
            self.x += 10 

    def jump(self,dir):        
        if dir == 0:   #left
            if self.is_move == True:
               self.x -= 10
            if self.jump_loop_count < 10:
               self.y -= 20
            else:
               self.y += 20 
        elif dir == 1:
            if self.is_move == True:
               self.x += 10
            if self.jump_loop_count < 10:
               self.y -= 20
            else:
               self.y += 20 

        self.jump_loop_count += 1
        if self.jump_loop_count >= 20:
            self.jump_loop_count = 0
            self.is_jump = False



pygame.init()
screen = pygame.display.set_mode((800,600))
rockman = pygame.image.load('rockman_sprites.png')
back = pygame.image.load('rockman_back.png')

#effect = pygame.mixer.Sound('mario_sound.wav')

pygame.mixer.music.load('rockman.mp3')
pygame.mixer.music.play(-1)

rockman.set_colorkey((0,0,0))

rock_obj = Rockman()      #สร้าง object

rock_obj.x = 65
rock_obj.y = 533

left_r = pygame.Rect(462,34,69,71)   
right_r = pygame.Rect(549,34,69,71)
left_jump = pygame.Rect(365,126,88,91)
right_jump = pygame.Rect(571,126,88,91)
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rock_obj.dir = 0                
                rock_obj.is_move = True                
            elif event.key == pygame.K_RIGHT:
                rock_obj.dir = 1                
                rock_obj.is_move = True               
            elif event.key == pygame.K_SPACE:
                rock_obj.is_jump = True
            else:
                rock_obj.is_move = False
        elif event.type == pygame.KEYUP:
            rock_obj.is_move = False

    screen.blit(back,(0,0))
    if rock_obj.is_move == True:
        if rock_obj.dir == 0:
            rock_obj.x -= 8
        elif rock_obj.dir == 1:
            rock_obj.x += 8

    if rock_obj.is_jump == True:
        rock_obj.jump(rock_obj.dir)

    if rock_obj.dir == 0:
       if rock_obj.is_jump == True:
           screen.blit(rockman,(rock_obj.x,rock_obj.y),left_jump)
       else:
           screen.blit(rockman,(rock_obj.x,rock_obj.y),left_r)
    elif rock_obj.dir == 1:
       if rock_obj.is_jump == True:
           screen.blit(rockman,(rock_obj.x,rock_obj.y),right_jump)
       else:
           screen.blit(rockman,(rock_obj.x,rock_obj.y),right_r)
           

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
