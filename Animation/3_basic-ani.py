from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WS=500
FPS=60
x=0.0
y=0.0

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WS,WS,-WS,WS)

def drawLines(x,y):
    # glBegin(GL_POINTS)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x+0.0,0.0)
    glVertex2f(x+100.0,100.0)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x+0.0,0.0)
    glVertex2f(x+100.0,-100.0)
    glEnd()

def drawPoly(x,y):
    glBegin(GL_POLYGON)
    glColor3f(1.0,0.0,1.0)
    glVertex2f(x+100.0,100.0)
    glVertex2f(-100.0+x,100.0)
    glVertex2f(-100.0+x,-100.0)
    glVertex2f(x+100.0,-100.0)
    glEnd()

def display():
    global x
    global y

    glClear(GL_COLOR_BUFFER_BIT)
	
    # glPointSize(5)
    
	#call drawFns
    
    drawPoly(x,y)
    glLineWidth(10)
    drawLines(x,y)

    glutSwapBuffers()

def animate(temp):
    global WS
    global FPS
    global x
    global y

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

    if(x+100>WS) :
        x=-400
    else:
        x=x+1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)

    glutCreateWindow("shapes-inro")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()