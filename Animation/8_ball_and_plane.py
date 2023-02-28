from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500
x=0
y=0
angle=45
FPS=60

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawLine(x,y,angle):
    x1=50*math.cos(math.pi*angle/180.0)+275-x
    y1=50*math.sin(math.pi*angle/180.0)+350-y
    glBegin(GL_LINES)
    glVertex2f(-500,-500)
    glVertex2f(350,350)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x1,y1)
    glVertex2f(275-x,350-y)
    glEnd()

def drawCircle(x,y):
    i=0
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(275-x,350-y)
    for i in range(0,361,1):
        glVertex2f(50*math.cos(math.pi*i/180.0)+275-x,50*math.sin(math.pi*i/180.0)+350-y)
    glEnd()

def display():
    global x
    global y
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    #draw functions
    drawCircle(x,y)
    drawLine(x,y,angle)
    glutSwapBuffers()

def animate(temp):
    global x
    global y
    global angle
    global WS
    global FPS

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

    if((275-x)<-WINDOW_SIZE):
        x=0
        y=0
        angle=45
    else:
        x=x+2
        y=y+2
        angle=angle+5

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE) 
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)

    glutCreateWindow("Window")
    
    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()

main()