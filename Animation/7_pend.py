from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WS=500
t=0
d=1

l=int(input("Enter length of pendulum : "))
r=int(input("Enter radius of bob : "))
tmax=int(input("Enter max angle of rotation : "))

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WS,WS,-WS,WS)

def drawLine():
    x1=-l
    y1=-l
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x1*math.cos(math.pi*t/180.0)-y1*math.sin(math.pi*t/180),x1*math.sin(math.pi*t/180)+y1*math.cos(math.pi*t/180.0))
    glEnd()

def drawCircle(t):
    i=0 
    cx1=-l
    cy1=-l
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx1*math.cos(math.pi*t/180.0)-cy1*math.sin(math.pi*t/180),cx1*math.sin(math.pi*t/180)+cy1*math.cos(math.pi*t/180.0))
    for i in range(0,361,1):
        x1=r*math.cos(math.pi*i/180.0)-l
        y1=r*math.sin(math.pi*i/180.0)-l
        glVertex2f(x1*math.cos(math.pi*t/180.0)-y1*math.sin(math.pi*t/180),x1*math.sin(math.pi*t/180)+y1*math.cos(math.pi*t/180.0))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global t
    #calls
    drawLine()
    drawCircle(t)

    glutSwapBuffers()

def animate(temp):
    global t
    global tmax
    global d
    glutPostRedisplay()
    glutTimerFunc(250,animate,int(0))
    if (d==1):
        if(t<tmax+45):
            t=t+5
        else:
            d=-1
    else:
        if(t>-tmax+45):
            t=t-5
        else:
            d=1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)

    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pendulum")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()