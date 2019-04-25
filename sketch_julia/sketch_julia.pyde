from math import sqrt, degrees,atan2, sin, cos,radians

#range of x-values
xmin = -2
xmax = 2

#range of y-values
ymin = -2
ymax = 2

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl,yscl
    size(600,600)
    noStroke()
    colorMode(HSB)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    translate(width/2,height/2)
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            z = [x,y]
            c = [-0.8,0.156]
            col=julia(z,c,100)
            if col == 100:
                fill(0)
            else:
                fill(3*col,255,255)
            rect(x*xscl,y*yscl,1,1)
            y += 0.01
        x += 0.01
    
def julia(z,c,num):
    count=0
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1,z1),c)
        count+=1
    return num

def arange(start,stop,step):
    '''returns a list of numbers from start to stop by step'''
    output = []
    x = start
    while x < stop:
        output.append(x)
        x += step
    return output

def cAdd(a,b):
    '''adds two complex numbers'''
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    '''returns the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]

def theta(z):
    '''calculates angle of rotation of a complex number'''
    return degrees(atan2(z[1],z[0]))

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
