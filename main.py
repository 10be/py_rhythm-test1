#main.py
import pygame, sys #외장함수 불러오기
from pygame.locals import *
from data import *

pygame.init()

size= (1280, 720) # 화면 크기 설정
FPS= 60 #프레임 수 변수

screen= pygame.display.set_mode(size) # size변수만큼의 크기의 창 생성 
pygame.display.set_caption('PY RHYTHM') # 게임 창의 이름 설정
fpsclock= pygame.time.Clock() # 프레임 조절을 위한 변수

n_line= sprite() # 클래스 불러오기(while문 밖에 할당)
n_line.insertImg('images/line.png') # 이미지 위치/이미지 파일명
n_line.setSize(512, 32) # 오브젝트 크기할당
n_line.x= 400 # 오브젝트 x좌표할당
n_line.y= 550 # 오브젝트 y좌표할당

while True: # 무한히 반복
    screen.fill((0, 0, 0)) # 배경 색 지정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    n_line.show()

    pygame.display.update() # 게임 창 유지
    fpsclock.tick(FPS) # FPS 변수 만큼의 프레임으로 지정