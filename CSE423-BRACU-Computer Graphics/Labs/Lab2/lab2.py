from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def find_zone(x1,y1,x2,y2):
    print("\n---find zone start---\n")
    print('x1 , y1 = {0}, {1}'.format(x1, y1))
    print('x2 , y2 = {0}, {1}\n'.format(x2, y2))

    # define
    x = x1
    y = y1
    zone = 0
    # dx & dy
    dx = x2 - x1
    dy = y2 - y1
    print('dx = {0} and dy = {1}'.format(dx, dy))
    print("\n")

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx > 0 and dy < 0:
            zone = 7
        elif dx < 0 and dy < 0:
            zone = 4

    else:
        if dx > 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx > 0 and dy < 0:
            zone = 6
        elif dx < 0 and dy < 0:
            zone = 5
    print('Zone = {}'.format(zone))
    print("\n---find zone end---\n")
    return zone

def convert_to_zone0(x,y,zone_to_convert):
    print("\n---conversion start---\n")
    converted_x = x
    converted_y = y
    match zone_to_convert:
        case 1:
            converted_x = y
            converted_y = x
        case 2:
            converted_x = y
            converted_y = -x
        case 3:
            converted_x = -x
            converted_y = y
        case 4:
            converted_x = -x
            converted_y = -y
        case 5:
            converted_x = -y
            converted_y = -x
        case 6:
            converted_x = -y
            converted_y = x
        case 7:
            converted_x = x
            converted_y = -y
    print('Converted = {0}, {1}'.format(converted_x, converted_y))
    print("\n---conversion end---\n")
    return converted_x, converted_y

def convert_back(x,y,zone_to_convert):
    print("\n---back conversion start---\n")
    converted_x = x
    converted_y = y
    match zone_to_convert:
        case 1:
            converted_x = y
            converted_y = x
        case 2:
            converted_x = -y
            converted_y = x
        case 3:
            converted_x = -x
            converted_y = y
        case 4:
            converted_x = -x
            converted_y = -y
        case 5:
            converted_x = -y
            converted_y = -x
        case 6:
            converted_x = y
            converted_y = -x
        case 7:
            converted_x = x
            converted_y = -y
    print('Converted back = {0}, {1}'.format(converted_x, converted_y))
    print("\n---back conversion end---\n")
    return converted_x, converted_y

def midpoint_line(x1,y1,x2,y2):
    print("\n---midpoint line start---\n")
    print('x1 , y1 = {0}, {1}'.format(x1, y1))
    print('x2 , y2 = {0}, {1}\n'.format(x2, y2))

    # saving all the points
    coordinates_array = []

    # define
    x = x1
    y = y1

    # dx & dy
    dx = x2 - x1
    dy = y2 - y1
    print('dx = {0} and dy = {1}'.format(dx, dy))
    print("\n")

    print("---x={}---\n".format(x))
    # decision parameter d
    d = (2 * dy) - dx
    print('D = {}'.format(d))
    print('x1 , y1 = {0}, {1}'.format(x1, y1))
    coordinates_array.append((x1,y1))
    print("\n--------")


    x +=1
    while x <= x2:
        print("---x={}---\n".format(x))
        # Midpoint below the line
        if d > 0:
            # choose upper pixel (NE)
            d = d + 2 * (dy - dx)
            print('D = {}'.format(d))
            y = y + 1
            print('x , y = {0}, {1}'.format(x,y))
        # Midpoint above the line
        else:
            # choose lower pixel (E)
            d = d + (2 * dy)
            print('D = {}'.format(d))
            print('x , y = {0}, {1}'.format(x, y))
        coordinates_array.append((x, y))
        x+=1
        print("\n--------")
    print("\n---midpoint line end---\n")
    return coordinates_array

def generate_pixels(x1,y1,x2,y2):
    found_zone = find_zone(x1,y1,x2,y2)

    if found_zone == 0:
        pixels = midpoint_line(x1,y1,x2,y2)
    else:
        converted1 = convert_to_zone0(x1,y1, found_zone)
        converted2 = convert_to_zone0(x2,y2, found_zone)
        pixels = midpoint_line(*converted1,*converted2)
        reverted = []
        for i in range(len(pixels)):
            reverted.append(convert_back(pixels[i][0], pixels[i][1], found_zone))
        pixels = reverted
    print('Pixels: \n {}'.format(pixels))
    return pixels

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 400, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    # make sure to not give x1==x2 or y1==y2
    # 3
    generated_pixels = generate_pixels(250, 400, 251, 200)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(150, 400, 250, 401)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(150, 300, 250, 301)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(150, 200, 250, 201)
    for p in generated_pixels:
        draw_points(*p)
    # 9
    generated_pixels = generate_pixels(400, 400, 401, 200)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(300, 400, 400, 401)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(300, 300, 400, 301)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(300, 200, 400, 201)
    for p in generated_pixels:
        draw_points(*p)
    generated_pixels = generate_pixels(300, 400, 301, 300)
    for p in generated_pixels:
        draw_points(*p)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2 (18301239)") #window name
glutDisplayFunc(showScreen)

glutMainLoop()