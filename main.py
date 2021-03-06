from Parse import Parse as p
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import sys
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders


test = p(sys.argv[1])
test.parse()
vl = test.vert_list
fl = test.face_list
vert_name = str(input('Enter name of vertex shader: '))
frag_name = str(input('Enter name of fragment shader: '))
class GLContext():
	def __init__(self, screen):
		self.rot_x = 0
		self.rot_y = 0
		self.lines = False
		self.pause = False
		# glEnable(GL_LIGHTING)
		# glEnable(GL_LIGHT0)
		vs_source=open('shaders/'+vert_name, "r")
		vs_source=vs_source.read()
		VERTEX_SHADER=shaders.compileShader(vs_source, GL_VERTEX_SHADER)										    

		fs_source=open('shaders/'+frag_name, "r")
		fs_source=fs_source.read()
		FRAGMENT_SHADER=shaders.compileShader(fs_source,GL_FRAGMENT_SHADER)

		self.shader=shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)

		# glLightModelfv(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
		shaders.glUseProgram(self.shader)
		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LEQUAL)
		light_position = [ 0.0, -1.0, 1.0, 1.0 ]
		glLightfv(GL_LIGHT0, GL_POSITION, light_position)
		glShadeModel(GL_SMOOTH)
		self.screen=screen
		self.aspect = screen.get_width()/screen.get_height()
		gluPerspective(45.0, self.aspect, 0.1, 200.0)

		glClearColor(0.0, 0.0, 0.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		return

	
	def check_events(self):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
				exit()
			if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
				self.lines = not self.lines
			if event.type == pygame.KEYUP and event.key == pygame.K_p:
				self.pause = not self.pause
		return

	def moving(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.rot_x -= 2
		if keys[pygame.K_DOWN]:
			self.rot_x += 2
		if keys[pygame.K_LEFT]:
			self.rot_y -= 2
		if keys[pygame.K_RIGHT]:
			self.rot_y += 2
		else:
			if not self.pause:
				self.rot_y += 1
		return

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glTranslatef(0.0, -.5, -3.0) 
		glRotatef(self.rot_x, 1, 0, 0)  
		glRotatef(self.rot_y, 0, 1, 0) 
		glRotatef(0.0, 0, 0, 1) 
		# glEnable(GL_LIGHTING)
		glBegin(GL_TRIANGLES)
		
		glColor3f(1.0, 0.0, 1.0)
		
		for x in range(len(fl)): #x starts at 0
			glNormal3f(vl[fl[x][1]][3], vl[fl[x][1]][4], vl[fl[x][1]][5])
			glVertex3f(vl[fl[x][1]][0], vl[fl[x][1]][1], vl[fl[x][1]][2])
			glNormal3f(vl[fl[x][2]][3], vl[fl[x][2]][4], vl[fl[x][2]][5])
			glVertex3f(vl[fl[x][2]][0], vl[fl[x][2]][1], vl[fl[x][2]][2])
			glNormal3f(vl[fl[x][3]][3], vl[fl[x][3]][4], vl[fl[x][3]][5])
			glVertex3f(vl[fl[x][3]][0], vl[fl[x][3]][1], vl[fl[x][3]][2])


		glEnd()
		
		if self.lines:
			glColor3f(1.0, 1.0, 1.0)
			for x in range(len(fl)): #x starts at 0
				glDisable(GL_LIGHTING)
				glBegin(GL_LINE_LOOP)
				glVertex3f(vl[fl[x][1]][0], vl[fl[x][1]][1], vl[fl[x][1]][2])
				glVertex3f(vl[fl[x][2]][0], vl[fl[x][2]][1], vl[fl[x][2]][2])
				glVertex3f(vl[fl[x][3]][0], vl[fl[x][3]][1], vl[fl[x][3]][2])
				glEnd()

		glPopMatrix()
		self.moving()
		return


def main():
	pygame.init() 
	screen = pygame.display.set_mode((600,600), pygame.OPENGL|pygame.DOUBLEBUF) 
	context=GLContext(screen) 

	
	while True:
		context.check_events() 
		context.display() 
		pygame.display.flip() 


if __name__ == '__main__':
	try:
		main()
	finally:
		pygame.quit()

