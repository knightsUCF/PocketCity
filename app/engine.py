import pygame
import window 
import render
import inputmgr
import updatestate
import synctime

import time
timestamp = time.time()

import datetime



import log
io = log.log()

GameRender = render.render()
GameInputMgr = inputmgr.inputmgr()
GameUpdateState = updatestate.updatestate()
GameSyncTime = synctime.synctime()




class engine():

    def run(self):
        #  gameWindow = window.window()
        #  gameWindow.Initialize()
        return 

    def gameloop(self):
        running = True
        while running:
            ''' io.o('Walking down the sidewalk...')
            timestampstring = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print('The time is now ', timestampstring) '''

            # WORKS: print(datetime.datetime.now())
            # THIS IS THE SCOPE YOU NEED TO COTNINUOUSLY UPDATE OUSTIDE OF ON EVENT PYGAME LOOP
          
            GameRender.update()

            print('getting state of input event')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                ''' GAME LOOP 
                
                A) initialize <-- happens in pocketcity.py

                B) render

                C) inputmgr

                D) updatestate

                E) synctime


                '''    

                

                ''' io.o('Walking down the sidewalk...')
                timestampstring = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print('The time is now ', timestampstring) '''
          







        
     
                
