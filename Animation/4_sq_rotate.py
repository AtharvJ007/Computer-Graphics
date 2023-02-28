from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WS=500
FPS=60
angle=0

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WS,WS,-WS,WS)

def drawSquare():
    glBegin(GL_QUADS)
    glVertex2f(150,0)
    glVertex2f(0,0)
    glVertex2f(0,150)
    glVertex2f(150,150)
    # glVertex2f(150,150)
    # glVertex2f(-150,150)
    # glVertex2f(-150,-150)
    # glVertex2f(150,-150)
    glEnd()

def drawLine():
    glLineWidth(5)
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(0,400)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawSquare()
    # drawLine()
    #draw functions
    glutSwapBuffers()

def animate(temp):
    glutPostRedisplay()
    glutTimerFunc(250,animate,int(0))
    glRotatef(45,0,0,1)
    # glScalef(0.8,0.8,0)
    # glTranslatef(1,1,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)

    glutCreateWindow("Square")
    
    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()

main()