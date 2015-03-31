from OpenGL import GLUT

class Application(object):
	def __init__(self, title="PyGL Application", position=(0,0), size=(640, 480), fullscreen=False, mouse=True):
		GLUT.glutInit()
		GLUT.glutInitDisplayMode(GLUT.GLUT_DOUBLE | GLUT.GLUT_RGB | GLUT.GLUT_DEPTH)
		GLUT.glutInitWindowPosition(*position)
		GLUT.glutInitWindowSize(*size)
		self.win_id = GLUT.glutCreateWindow(title)
		GLUT.glutDisplayFunc(self.display)
		if mouse:
			self.mouse_pos = (0,0)
			GLUT.glutMouseFunc(self.mouse)
		if fullscreen:
			GLUT.glutFullScreen()

	def start(self):
		GLUT.glutMainLoop()

	def display(self):
		pass

	def mouse(self, button, state, x, y):
		self.mouse_pos = (x, y)
		if state == GLUT.GLUT_DOWN:
			if button == GLUT.GLUT_LEFT_BUTTON:
				self.left_click()
			elif button == GLUT.GLUT_RIGHT_BUTTON:
				self.right_click()
			elif button == GLUT.GLUT_MIDDLE_BUTTON:
				self.middle_click()
			else:
				raise ValueError("Unknown button %s pressed" % str(button))
		elif state == GLUT.GLUT_UP:
			if button == GLUT.GLUT_LEFT_BUTTON:
				self.left_release()
			elif button == GLUT.GLUT_RIGHT_BUTTON:
				self.right_release()
			elif button == GLUT.GLUT_MIDDLE_BUTTON:
				self.middle_release()
			else:
				raise ValueError("Unknown button %s released" % str(button))

	def left_click(self):
		pass

	def left_release(self):
		pass

	def middle_click(self):
		pass

	def middle_release(self):
		pass

	def right_click(self):
		pass

	def right_release(self):
		pass

	def keyboard(self, key, x, y):
		pass