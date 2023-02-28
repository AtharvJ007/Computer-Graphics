from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WS=500
x1=-400
x2=400

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-WS,WS,-WS,WS)

#fns
def drawCircle(x,s):
    if (s==0):  
        i=0
        glColor3f(1,0,0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0+x1,0)
        for i in range(0,361,1) :
            glVertex2f(100*math.cos(i*math.pi/180.0)+x1,100*math.sin(i*math.pi/180.0))
        glEnd()
    if (s==1):  
        i=0
        glColor3f(0,0,1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0+x2,0)
        for i in range(0,361,1) :
            glVertex2f(100*math.cos(i*math.pi/180.0)+x2,100*math.sin(i*math.pi/180.0))
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global x1
    global x2
    #fn call
    drawCircle(x1,0)
    drawCircle(x2,1)

    glutSwapBuffers()

def animate(temp):
    global x1
    global x2

    glutPostRedisplay()
    glutTimerFunc(250,animate,int(0))

    x1=x1+10
    x2=x2-10

    if(x1>400):
        x1=-400
    if(x2<-400):
        x2=400

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WS,WS)
    glutCreateWindow("Passing circles")

    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()