from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# this draws n number of pixels
def draw_pixels(n):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)

    for i in range(n):
        # generates n numbers of both x and y coordinates for n pixels
        x = random.randrange(0, 500, 3)
        y = random.randrange(0, 500, 3)
        print('{0}. (x,y) = {1},{2}'.format(i+1,x,y))
        glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_pixels(50)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 1") #window name
glutDisplayFunc(showScreen)

glutMainLoop()