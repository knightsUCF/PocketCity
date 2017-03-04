import pyglet


# http://pyglet-current.readthedocs.io/en/latest/programming_guide/quickstart.html

class window(pyglet.window.Window):
	
	def __init__(self, xs, ys):
		self.GameInstance = Board(xs, ys)
		super().__init__(width = 512, height = 512, visible = False)

    def on_draw(self):
        self.clear()


'''


	def SetupWindow(self):
		
		print("Hello world")
		window = pyglet.window.Window()
		label = pyglet.text.Label('Hello, world',
			font_name = 'Times New Roman',
			font_size = 36, 
			x = window.width//2, y = window.height//2,
			anchor_x = 'center', anchor_y = 'center')
        @window.event
        def on_draw():
        	window.clear()
        	label.draw()

        pyglet.app.run()

'''


