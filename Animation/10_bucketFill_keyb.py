from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WS=500
y=0
ty=0

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-WS,WS,-WS,WS)

def drawLine():
    glLineWidth(7)
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(-100,200)
    glVertex2f(-100,0)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(100,0)
    glVertex2f(100,200)
    glEnd()

def drawQuad():
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(100,y)
    glVertex2f(-100,y)
    glEnd()

def drawdrops(x1,y1,ty):
    i=0
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,1)
    glVertex2f(x1,y1+20-ty)
    for i in range(0,360,1):
        glVertex2f(5*math.cos(math.pi*i/180.0)-5*math.sin(math.pi*i/180.0)+x1,5*math.cos(math.pi*i/180.0)+5*math.sin(math.pi*i/180.0)+y1-ty)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # call
    drawQuad()
    drawLine()
    drawdrops(0,510,ty)
    drawdrops(-30,550,ty)
    drawdrops(-70,570,ty)
    drawdrops(80,600,ty)
    glutSwapBuffers()

def keyboard(key,x,y):
    key=key.decode()

    if(key=='a'):
        animate(5,'a')

    elif(key=='s'):
        animate(-5,'s')

    elif(key=='f'):
        glutFullScreen()

    elif(key=='q'):
        glutLeaveMainLoop()

#animate

def animate(value,key):
    global y
    global ty

    if(key=='a'):
        if(y>=200):
            y=200
        else:
            y=y+value
            if(ty<450):
                ty=ty+150
            else:
                ty=0

    elif(key=='s'):
        ty=0
        if(y<=0):
            y=0
        else:
            y=y+value

    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)

    glutInitWindowSize(WS,WS)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Window")

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(display)

    init()
    glutMainLoop()
main()
