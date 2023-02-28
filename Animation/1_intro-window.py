from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE=500

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    #draw functions
    #glutSwapBuffers()  OR glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE) # | GLUT_DOUBLE
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)

    glutCreateWindow("Window")
    
    glutDisplayFunc(display)
    #glutTimerFunc(0,animate,0)
    #glutIdleFunc(display)

    init()
    glutMainLoop()

main()