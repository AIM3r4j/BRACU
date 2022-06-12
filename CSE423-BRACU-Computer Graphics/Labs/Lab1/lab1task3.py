from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dda(x1,y1,x2,y2):
    glPointSize(4)
    print("\n---dda start---\n")
    print('x1 , y1 = {0}, {1}'.format(x1,y1))
    print('x2 , y2 = {0}, {1}\n'.format(x2,y2))

    # define
    x = x1
    y = y1

    # dx & dy
    dx = x2 - x1
    dy = y2 - y1
    print('dx = {0} and dy = {1}'.format(dx,dy))
    print("\n")

    # steps required
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    glBegin(GL_POINTS)
    if x1 == x2 and y1 < y2:
        for s in range(steps):
            y = y + 1
            glVertex2f(x, y)
            print('x , y = {0}, {1}'.format(x, y))
    elif x1 == x2 and y1 > y2:
        for s in range(steps):
            y = y - 1
            glVertex2f(x, y)
            print('x , y = {0}, {1}'.format(x, y))
    elif y1 == y2 and x1 < x2:
        for s in range(steps):
            x = x + 1
            glVertex2f(x, y)
            print('x , y = {0}, {1}'.format(x, y))
    elif y1 == y2 and x1 > x2:
        for s in range(steps):
            x = x - 1
            glVertex2f(x, y)
            print('x , y = {0}, {1}'.format(x, y))
    else:
        # slope m
        m = dy/dx
        m = round(m, 2)
        print('m = {0} and 1/m = {1}'.format(m, 1/m))
        print("\n")

        for s in range(steps):
            print('----{}----\n'.format(s))
            if x1 > x2 and y1 > y2:
                if -1 < m < 1:
                    x = x - 1
                    print('x = {}'.format(x))
                    y = y - m
                    glVertex2f(x, round(y))
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x - (1 / m)
                    print('x = {}'.format(x))
                    y = y - 1
                    glVertex2f(round(x), y)
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 > x2 and y1 < y2:
                if -1 < m < 1:
                    x = x - 1
                    print('x = {}'.format(x))
                    y = y - m
                    glVertex2f(x, round(y))
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x + (1 / m)
                    print('x = {}'.format(x))
                    y = y + 1
                    glVertex2f(round(x), y)
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 < x2 and y1 > y2:
                if -1 < m < 1:
                    x = x + 1
                    print('x = {}'.format(x))
                    y = y + m
                    glVertex2f(x, round(y))
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x - (1 / m)
                    print('x = {}'.format(x))
                    y = y - 1
                    glVertex2f(round(x), y)
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 < x2 and y1 < y2:
                if -1 < m < 1:
                    x = x + 1
                    print('x = {}'.format(x))
                    y = y + m
                    glVertex2f(x, round(y))
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x + (1 / m)
                    print('x = {}'.format(x))
                    y = y + 1
                    glVertex2f(round(x), y)
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))

            print('\n----------\n')
    glEnd()
    print('\n-----dda end-----\n')

def dda_dotted_line(x1,y1,x2,y2):
    glPointSize(3)
    gap_creator = 1
    print("\n---dda dotted start---\n")
    print('x1 , y1 = {0}, {1}'.format(x1, y1))
    print('x2 , y2 = {0}, {1}\n'.format(x2, y2))

    # define
    x = x1
    y = y1

    # dx & dy
    dx = x2 - x1
    dy = y2 - y1
    print('dx = {0} and dy = {1}'.format(dx, dy))
    print("\n")

    # steps required
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    glBegin(GL_POINTS)
    if x1 == x2 and y1 < y2:
        for s in range(steps):
            y = y + 1
            if gap_creator % 8 == 0:
                glVertex2f(x, y)
            gap_creator = gap_creator + 1
            print('x , y = {0}, {1}'.format(x, y))
    elif x1 == x2 and y1 > y2:
        for s in range(steps):
            y = y - 1
            if gap_creator % 8 == 0:
                glVertex2f(x, y)
            gap_creator = gap_creator + 1
            print('x , y = {0}, {1}'.format(x, y))
    elif y1 == y2 and x1 < x2:
        for s in range(steps):
            x = x + 1
            if gap_creator % 8 == 0:
                glVertex2f(x, y)
            gap_creator = gap_creator + 1
            print('x , y = {0}, {1}'.format(x, y))
    elif y1 == y2 and x1 > x2:
        for s in range(steps):
            x = x - 1
            if gap_creator % 8 == 0:
                glVertex2f(x, y)
            gap_creator = gap_creator + 1
            print('x , y = {0}, {1}'.format(x, y))
    else:
        # slope m
        m = dy / dx
        m = round(m, 2)
        print('m = {0} and 1/m = {1}'.format(m, 1 / m))
        print("\n")

        for s in range(steps):
            print('----{}----\n'.format(s))
            if x1 > x2 and y1 > y2:
                if -1 < m < 1:
                    x = x - 1
                    print('x = {}'.format(x))
                    y = y - m
                    if gap_creator % 8 == 0:
                        glVertex2f(x, round(y))
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x - (1 / m)
                    print('x = {}'.format(x))
                    y = y - 1
                    if gap_creator % 8 == 0:
                        glVertex2f(round(x), y)
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 > x2 and y1 < y2:
                if -1 < m < 1:
                    x = x - 1
                    print('x = {}'.format(x))
                    y = y - m
                    if gap_creator % 8 == 0:
                        glVertex2f(x, round(y))
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x + (1 / m)
                    print('x = {}'.format(x))
                    y = y + 1
                    if gap_creator % 8 == 0:
                        glVertex2f(round(x), y)
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 < x2 and y1 > y2:
                if -1 < m < 1:
                    x = x + 1
                    print('x = {}'.format(x))
                    y = y + m
                    if gap_creator % 8 == 0:
                        glVertex2f(x, round(y))
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x - (1 / m)
                    print('x = {}'.format(x))
                    y = y - 1
                    if gap_creator % 8 == 0:
                        glVertex2f(round(x), y)
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))
            elif x1 < x2 and y1 < y2:
                if -1 < m < 1:
                    x = x + 1
                    print('x = {}'.format(x))
                    y = y + m
                    if gap_creator % 8 == 0:
                        glVertex2f(x, round(y))
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('y rounded = {}'.format(round(y)))
                    print('x , y = {0}, {1}'.format(x, round(y)))
                else:
                    x = x + (1 / m)
                    print('x = {}'.format(x))
                    y = y + 1
                    if gap_creator % 8 == 0:
                        glVertex2f(round(x), y)
                    gap_creator = gap_creator + 1
                    print('y = {}'.format(y))
                    print('x rounded = {}'.format(round(x)))
                    print('x , y = {0}, {1}'.format(round(x), y))

            print('\n----------\n')
    glEnd()
    print('\n-----dda dotted end-----\n')


def draw_tails():
    dda(200, 100, 200, 400)
    dda_dotted_line(40, 400, 360, 400)

def draw_heads():
    dda_dotted_line(100, 100, 100, 400)
    dda(100,250, 300, 250)
    dda(300, 100, 300, 400)

def toss_the_coin(std_id):
    if int(std_id[-1]) % 2 == 0 :
        draw_tails()
        print("Output: Tails")
    else:
        draw_heads()
        print("Output: Heads")


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

    student_id = "18301239" # declare the student id here
    toss_the_coin(student_id)
    print("Student ID: {}".format(student_id))

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(450, 450) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 3") #window name
glutDisplayFunc(showScreen)

glutMainLoop()