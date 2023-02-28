from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WS=500
t=0
s=2

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WS,WS,-WS,WS)

def drawquad(t,s):
    x1=100
    y1=100
    glBegin(GL_QUADS)
    glVertex2f(s*(x1*math.cos(math.pi*t/180.0)-y1*math.sin(math.pi*t/180)),s*(x1*math.sin(math.pi*t/180)+y1*math.cos(math.pi*t/180.0)))
    glVertex2f(s*(-x1*math.cos(math.pi*t/180.0)-y1*math.sin(math.pi*t/180)),s*(-x1*math.sin(math.pi*t/180)+y1*math.cos(math.pi*t/180.0)))
    glVertex2f(s*(-x1*math.cos(math.pi*t/180.0)+y1*math.sin(math.pi*t/180)),s*(-x1*math.sin(math.pi*t/180)-y1*math.cos(math.pi*t/180.0)))
    glVertex2f(s*(x1*math.cos(math.pi*t/180.0)+y1*math.sin(math.pi*t/180)),s*(x1*math.sin(math.pi*t/180)-y1*math.cos(math.pi*t/180.0)))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global t
    global s
    drawquad(t,s)
    glutSwapBuffers()

#animate
def animate(temp):
    global t
    global s
    glutPostRedisplay()
    glutTimerFunc(250,animate,int(0))
    if(s<-2):
        s=2
    else:
        s=s-0.05
    if(s<0):
        t=t-10
    else:
        t=t+10

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)

    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Window")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()
