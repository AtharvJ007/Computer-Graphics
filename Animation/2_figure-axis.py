from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WS=500

def init():
	glClearColor(0.0,0.0,0.0,1.0)
	gluOrtho2D(-WS,WS,-WS,WS)

def drawLines():
    # glBegin(GL_POINTS)
    glLineWidth(10)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(0.0,0.0)
    glVertex2f(100.0,100.0)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(0.0,0.0)
    glVertex2f(100.0,-100.0)
    glEnd()

def drawPoly():
    glBegin(GL_POLYGON)
    glColor3f(1.0,0.0,1.0)
    glVertex2f(100.0,100.0)
    glVertex2f(-100.0,100.0)
    glVertex2f(-100.0,-100.0)
    glVertex2f(100.0,-100.0)
    glEnd()

def drawCircle():
    glColor3f(0.0,0.0,1.0)
    i=0
    glBegin(GL_TRIANGLE_FAN) #GL_POLYGON
    glVertex2f(0,0)
    for i in range(0,1000,1):
        glVertex2f(75*math.cos(math.pi*i/180.0)+100,75*math.sin(math.pi*i/180.0)+100)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
	
    # glPointSize(5)
    
	#call drawFns
    
    drawPoly()
    drawCircle()
    drawLines()

    glutSwapBuffers()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

	glutInitWindowSize(WS,WS)
	glutInitWindowPosition(0,0)

	glutCreateWindow("shapes-inro")

	glutDisplayFunc(display)

	init()
	glutMainLoop()
main()