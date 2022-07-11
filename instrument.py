import matplotlib.pyplot as plt
import numpy as np
import time
from print_array import *
import scipy.optimize as opt

class instrument:
    xmin=0; xmax=100; ymin=0; ymax=100 #boundaries for search
  
    def __init__(self,motorspeed,error,starttime):#s/steps,error for 1s integration time
        self.motorspeed=motorspeed
        self.error=error
        self.starttime=starttime
        self.t=0
        self.pos=np.array([self.xmin+np.random.uniform(0,self.xmax-self.xmin),self.ymin+np.random.uniform(0,self.ymax-self.ymin)])#random position
        self.x1=np.random.uniform(1,90)
        self.x2=np.random.uniform(1,90)
        self.sig1=np.random.uniform(5.0,10.0)
        self.sig2=np.random.uniform(5.0,10.0)
        self.theta=np.random.uniform(0,2*np.pi)
        self.func=lambda x: np.exp(-0.5*((((x[0]-self.x1)*np.cos(self.theta)-(x[1]-self.x2)*np.sin(self.theta))/self.sig1)**2+(((x[0]-self.x1)*np.sin(self.theta)+(x[1]-self.x2)*np.cos(self.theta))/self.sig2)**2))
 
    def scan(self,x,st):#position, scan time
        self.t+=(abs(x[0]-self.pos[0])+abs(x[1]-self.pos[1]))*self.motorspeed+st+self.starttime
        self.pos=np.array(x)
        return self.func(x)+np.random.normal(0,self.error,(1))[0]*(0.1+0.9*st**-.5)
    

MIM_LP_DOAS=instrument(50,0.01,0.5)
print 'measurement value at [20,30] for a integaration time of 10s:',MIM_LP_DOAS.scan([20,30],10)
