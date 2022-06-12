from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def midpoint_circle(r, center_x, center_y):
    print("\n---midpoint circle start---\n")
    print('radius = {}'.format(r))
    print('center = {0}, {1}'.format(center_x,center_y))

    # saving all the points
    slice_points = []

    # define
    x = 0
    y = r

    slice_points.append((x , y))

    print("\n---x={}---\n".format(x))
    # decision parameter d
    d = 5 - (4*r)
    print('D = {}'.format(d))
    print('original x , y = {0}, {1}'.format(x,  y))
    print('x , y = {0}, {1}'.format(x + center_x, y + center_y))
    print("\n--------")

    while x < y-1:
        print("---x={}---\n".format(x+1))
        if d >= 0:
            # choose lower pixel (SE)
            d = d + 2 * x - 2 * y + 5
            print('D = {}'.format(d))
            x = x + 1
            y = y - 1

        else:
            # choose upper pixel (E)
            d = d + 2 * x + 3
            print('D = {}'.format(d))
            x = x + 1
        print('original x , y = {0}, {1}'.format(x, y))
        print('x , y = {0}, {1}'.format(x + center_x, y + center_y))
        slice_points.append((x, y))
        print("\n--------")

    circle_points = get_other_points(slice_points, center_x, center_y)


    print("\n---midpoint circle end---\n")
    return circle_points

def get_other_points(slice_points, center_x, center_y):
    circle_points_array = []
    zone0_array = []
    zone1_array = []
    zone2_array = []
    zone3_array = []
    zone4_array = []
    zone5_array = []
    zone6_array = []
    zone7_array = []

    for s in range(len(slice_points)):
        x, y = slice_points[s][0], slice_points[s][1]
        zone0_array.append((y+ center_x, x+ center_y))
        zone1_array.append((x+ center_x, y+ center_y))
        zone2_array.append((-x+ center_x, y+ center_y))
        zone3_array.append((-y+ center_x, x+ center_y))
        zone4_array.append((-y+ center_x, -x+ center_y))
        zone5_array.append((-x+ center_x, -y+ center_y))
        zone6_array.append((x+ center_x, -y+ center_y))
        zone7_array.append((y+ center_x, -x+ center_y))

    circle_points_array.append(zone0_array)
    circle_points_array.append(zone1_array)
    circle_points_array.append(zone2_array)
    circle_points_array.append(zone3_array)
    circle_points_array.append(zone4_array)
    circle_points_array.append(zone5_array)
    circle_points_array.append(zone6_array)
    circle_points_array.append(zone7_array)

    return circle_points_array

def get_other_centers(radius):
    center = math.ceil(radius * math.cos(math.pi/4))
    center1 = (center,center)
    center2 = (-center, center)
    center3 = (center, -center)
    center4 = (-center, -center)
    return center1, center2, center3, center4

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 600, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-600, 600, -600, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here

    # Largest Circle
    radius1 = 500
    centerX = 0
    centerY = 0
    pixels = midpoint_circle(radius1, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Top Circle
    radius2 = (radius1/2)
    centerX = 0
    centerY = (radius1/2)
    pixels = midpoint_circle(radius2, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Bottom Circle
    radius3 = (radius1/2)
    centerX = 0
    centerY = -(radius1/2)
    pixels = midpoint_circle(radius3, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Left Circle
    radius4 = (radius1/2)
    centerX = -(radius1/2)
    centerY = 0
    pixels = midpoint_circle(radius4, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Right Circle
    radius5 = (radius1/2)
    centerX = (radius1/2)
    centerY = 0
    pixels = midpoint_circle(radius5, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Other 4 Circles
    center1, center2 , center3, center4 = get_other_centers(radius1/2)

    radius6 = (radius1 / 2)
    (centerX, centerY) = center1
    pixels = midpoint_circle(radius6, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius7 = (radius1 / 2)
    (centerX, centerY) = center2
    pixels = midpoint_circle(radius7, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius8 = (radius1 / 2)
    (centerX, centerY) = center3
    pixels = midpoint_circle(radius8, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius9 = (radius1 / 2)
    (centerX, centerY) = center4
    pixels = midpoint_circle(radius9, centerX, centerY)
    print(pixels)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 3") #window name
glutDisplayFunc(showScreen)

glutMainLoop()