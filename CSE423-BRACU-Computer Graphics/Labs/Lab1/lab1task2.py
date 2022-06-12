from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# this draws a house
def draw_house():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)

    # Roof
    glVertex2f(100, 250)
    glVertex2f(500, 250)

    glVertex2f(100, 250)
    glVertex2f(300, 350)

    glVertex2f(500, 250)
    glVertex2f(300, 350)

    # Wall
    glVertex2f(100, 250)
    glVertex2f(100, 20)

    glVertex2f(500, 250)
    glVertex2f(500, 20)

    glVertex2f(100, 20)
    glVertex2f(500, 20)

    # Windows
    glVertex2f(130, 210)
    glVertex2f(200, 210)

    glVertex2f(130, 210)
    glVertex2f(130, 150)

    glVertex2f(130, 150)
    glVertex2f(200, 150)

    glVertex2f(200, 210)
    glVertex2f(200, 150)

    glVertex2f(470, 210)
    glVertex2f(400, 210)

    glVertex2f(470, 210)
    glVertex2f(470, 150)

    glVertex2f(400, 150)
    glVertex2f(470, 150)

    glVertex2f(400, 210)
    glVertex2f(400, 150)

    # Door

    glVertex2f(250, 150)
    glVertex2f(350, 150)

    glVertex2f(250, 150)
    glVertex2f(250, 20)

    glVertex2f(350, 150)
    glVertex2f(350, 20)

    glEnd()

    # Door knob
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(330, 80)
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
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_house()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 450) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 2") #window name
glutDisplayFunc(showScreen)

glutMainLoop()