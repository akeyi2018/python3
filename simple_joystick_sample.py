import pygame
from pygame.locals import *
from time import sleep

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ('joystick start')

    pygame.init()

    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))
        sleep(0.1)
        

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ('joystickが見つかりませんでした。')
