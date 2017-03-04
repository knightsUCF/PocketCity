import window
import gridmgr
import state
import render 
import initialize
import engine
import log

io = log.log()

RunGameLoop = engine.engine()

NewGame = initialize.initialize()
NewGame.start()

io.o('\n\nYou have reached the end of the sidewalk! :)')


