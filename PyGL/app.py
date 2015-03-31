from OpenGL import GLUT

class Application(object):
	def __init__(self, display, title="PyGL Application", position=(0,0), size=(640, 480), fullscreen=False):
		GLUT.glutInit()
		GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB | GLUT.GLUT_DEPTH)
		GLUT.glutInitWindowPosition(*position)
		GLUT.glutInitWindowSize(*size)
		self.win_id = GLUT.glutCreateWindow(title)
		GLUT.glutDisplayFunc(display)

	def start(self):
		GLUT.glutMainLoop()
