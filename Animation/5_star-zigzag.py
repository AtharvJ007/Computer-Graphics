from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WS=500
theta=0
x=0
y=0

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-WS,WS,-WS,WS)

#functions
def drawCircle():
    glColor3f(1,0,0)
    i=0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,0)
    for i in range(0,361,1):
        glVertex2f(40*math.cos(i*(math.pi)/180),40*math.sin(i*(math.pi)/180))
        # glVertex2f(75*math.cos(math.pi*i/180.0),75*math.sin(math.pi*i/180.0))
    glEnd()

def drawStar():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(-30,30)
    glVertex2f(0,120)
    glVertex2f(30,30)
    glVertex2f(120,0)
    glVertex2f(30,-30)
    glVertex2f(0,-120)
    glVertex2f(-30,-30)
    glVertex2f(-120,0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    #call fns
    drawStar()
    drawCircle()
    glutSwapBuffers()

#animate
def animate(temp):
    theta
    global x
    global y
    glutPostRedisplay()
    glutTimerFunc(250,animate,int(0))
    # glRotatef(10,0,0,1)
    # glScalef(0.9,0.9,0)

    if x>-380 and y>=0:
        x=x+20
        glTranslatef(20,0,0)
    if x>380:
        x=0
        glTranslatef(-500,0,0)
        
    # glTranslatef(0,80,0)
    # print(x)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Star")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()