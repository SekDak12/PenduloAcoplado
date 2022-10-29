#Sistema PenDob acoplado a PenSim

from cmath import pi
from re import L
from scipy.integrate import odeint 
import math 
import numpy as np
import pylab as py
import matplotlib.pyplot as plt



m1 = 10000                 # Masa del primer pendulo
m2 = m1+1000000                  # Masa del segundo pendulo
L1 = 1.5                 # Longitud de la cuerda del primer pendulo
L2 = L1                  # Longitud de la cuerda del segundo pedulo
g = 9.81                # Gravedad 
u0 = [np.pi/2, 0, -np.pi/2, 0, np.pi, 0]    # Condiciones iniciales en forma vectorial
# (Angulo inicial 1er pendulo, velocidad 1er pendulo, angulo inicial 2do pendulo, velocidad 2do pendulo,angulo inicial 3do pendulo, velocidad 3do pendulo)
t = np.linspace(0, 60, 1000)  #Intervalo de solucion.
k= 30                  #Constante del resorte

def Pen_Acop(u,t,m1,m2,L1,L2,g, k):         #Definimos el sistema de ecuaciones diferenciales que describen el sistema

    du = np.zeros(6)    
    c = np.cos(u[0]-u[2])   #Coseno de diferenia de Thetha´s
    s = np.sin(u[0]-u[2])   #seno de diferenia de Thetha´s

    du[0] = u[1]   # d(theta 1) 
    du[1] = ( m2*g*np.sin(u[2])*c - m2*s*(L1*c*u[1]**2 + L2*u[3]**2) - (m1+m2)*g*np.sin(u[0]) ) /( L1 *(m1+m2*s**2) ) +(k/(2*m1*L1))*(np.sin(u[4])-np.sin(u[0])*np.cos(u[0]))
    du[2] = u[3]   # d(theta 2)   
    du[3] = ((m1+m2)*(L1*u[1]**2*s - g*np.sin(u[2]) + g*np.sin(u[0])*c) + m2*L2*u[3]**2*s*c) / (L2 * (m1 + m2*s**2))
    du[4] = u[5]   # d(theta 3)
    du[5] = (-g/L1)*np.sin(u[5])-k*L1*(np.sin(u[5])-np.sin(u[1])*np.cos(u[5]))
    
    
    return du
    
sol = odeint(Pen_Acop, u0, t, args=(m1,m2,L1,L2,g, k))
u0 = sol[:,0]    #  theta 1
u1 = sol[:,1]    # d(theta 1) 
u2 = sol[:,2]    #  theta 1
u3 = sol[:,3]    # d(theta 2) 
u4 = sol[:,4]    #  theta 1
u5 = sol[:,5]    # d(theta 3) 

# Cambio de coordenadas polares a cartesianas 

# Primer pendulo
x1 = L1*np.cos(u0);          
y1 = -L1*np.sin(u0);
# Segundo pendulo
x2 = x1 + L2*np.cos(u2);     
y2 = y1 - L2*np.sin(u2);
#Tercer Pendulo
x3 = L1*np.cos(u4);          
y3 = -L1*np.sin(u4);

#def Up(a,b):          #Energia Potencial del pendulo simple acoplado
#    return -m1*g*L*(np.cos(a))+((k)/(2))*(L*np.sin(a)-L*np.sin(b))*(L*np.sin(a)-L*np.sin(b))

#def K(c):          #Energia Cinetica del pendulo simple acoplado
#    return (1/2)*(m1*L*L*c*c)

def Upp(a,b,c):          #Energia Potencial del pendulo acoplado
    return -2*m1*g*L*(np.cos(a))-m1*g*L*(np.cos(b))+((k)/(2))*(L*np.sin(c)-L*np.sin(b))*(L*np.sin(c)-L*np.sin(b))-m1*g*L*(np.cos(c))

def Kk(a,b,c,e, f ):          #Energia Cinetica del pendulo acoplado
    return (1/2)*(2*m1*L*L*a*a+2*m1*L*L*a*b*np.cos(f-e)+m1*L*L*b*b+m1*L*L*c*c)


#Mapeo en el mapa cartesiano
plt.plot(x1,y1,'-',color = '#003ff5',label = r'Pendulo 1')    #Solucion de la primer ec dif
plt.plot(x2,y2,'-',color = '#f50000',label = r'Pendulo 2' )   #Solucion de la segunda ec dif
plt.plot(y3,x3+7,'-',color = '#000000',label = r'Pendulo 3')    #Solucion de la tecer ec dif
py.xlabel('x')
py.ylabel('y')
plt.legend(loc=1)
plt.xlim([0, 10])
plt.show()

#Mapeo velocidades de los pendulos
plt.plot(t,u0,'-',color = '#003ff5',label = r'\theta_1')    #Solucion de la primer ec dif
plt.plot(t,u2,'-',color = '#f50000',label = r'\theta_2' )   #Solucion de la segunda ec dif
plt.plot(t,u4,'-',color = '#000000',label = r'\theta_3')    #Solucion de la tecer ec dif
py.xlabel('t')
py.ylabel('Posicion angular')
plt.legend(loc=1)
plt.xlim([0, 40])
plt.show()


#Mapeo energias de los pendulos
plt.plot(t,Upp(u0,u2,u4),'-',color = '#003ff5',label = r'U')    #Energia potencial
plt.plot(t,Kk(u1,u3,u5,u0,u2 ),'-',color = '#f50000',label = r'T' )   #Energia Cinetica
#plt.plot(t,Kk(u1,u3,u5,u0,u2 )+Upp(u0,u2,u4),'-',color = '#000000',label = r'Energia Total' )   #Energia Cinetica
py.xlabel('Tiempo (t)')
py.ylabel('Energias (J)')
plt.legend(loc=1)
plt.xlim([0,40])
plt.show()
