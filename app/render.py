import state

import time
timestamp = time.time()

import datetime



import log
io = log.log()




class render():

    
    def draw(state):
        io.o('Getting state >>> >>> >>> >>> >>>') 
        ''' timestampstring = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print('The time is now ', timestampstring) '''
        print(datetime.datetime.now()) 


    def update(self):
        self.draw()
         









