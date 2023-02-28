from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WS=500
x=0
y=0
r=0
t=0

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WS,WS,-WS,WS)

# fns

def drawCircle(x,y,r,a):
    i=0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x*math.cos(math.pi*(t+a)/180.0)-y*math.sin(math.pi*(t+a)/180.0),x*math.sin(math.pi*(t+a)/180.0)+y*math.cos(math.pi*(t+a)/180.0))
    for i in range(0,361,1):
        x1=r*math.cos(math.pi*i/180.0)+x
        y1=r*math.sin(math.pi*i/180.0)+y
        glVertex2f(x1*math.cos(math.pi*(t+a)/180.0)-y1*math.sin(math.pi*(t+a)/180.0),x1*math.sin(math.pi*(t+a)/180.0)+y1*math.cos(math.pi*(t+a)/180.0))
    glEnd()

def drawPath(x,y):
    i=0
    glBegin(GL_POINTS)
    for i in range(0,360,5):
        glVertex2f(x*math.cos(math.pi*i/180.0)-y*math.sin(math.pi*i/180.0),x*math.sin(math.pi*i/180.0)+y*math.cos(math.pi*i/180.0))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    global r
    #calls
    glColor3f(1,1,0)
    drawCircle(0,0,80,0)

    glColor3f(1,1,1)
    drawPath(0,150)
    glColor3f(1,0,0)
    drawCircle(0,150,20,45)

    glColor3f(1,1,1)
    drawPath(0,250)
    glColor3f(0.5,0.0,0.5)
    drawCircle(0,250,40,120)
    glutSwapBuffers()

#animate
def animate(temp):
    global x
    global y
    global t

    glutPostRedisplay()
    glutTimerFunc(300,animate,int(0))

    t=t+20

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)

    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Solar_System")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()

main()