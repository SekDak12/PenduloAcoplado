from cmath import pi
from scipy.integrate import odeint 
import math 
import numpy as np
import pylab as py
import matplotlib.pyplot as plt



m1 = 10                  # Masa del primer pendulo
m2 = m1                  # Masa del segundo pendulo
L1 = 1                  # Longitud de la cuerda del primer pendulo
L2 = L1                  # Longitud de la cuerda del segundo pedulo
g = 9.81                # Gravedad 
u0 = [np.pi/2, 0, -np.pi, 0]    # Condiciones iniciales en forma vectorial
# (Angulo inicial 1er pendulo, velocidad 1er pendulo, angulo inicial 2do pendulo, velocidad 2do pendulo)
t = np.linspace(0, 60, 1000)  #Intervalo de solucion.


def Pen_dob(u,t,m1,m2,L1,L2,g):         #Definimos el sistema de ecuaciones diferenciales que describen el sistema

    du = np.zeros(4)    
    c = np.cos(u[0]-u[2])   #Coseno de diferenia de Thethas´s
    s = np.sin(u[0]-u[2])   #seno de diferenia de Thethas´s

    du[0] = u[1]   # d(theta 1)
    du[1] = ( m2*g*np.sin(u[2])*c - m2*s*(L1*c*u[1]**2 + L2*u[3]**2) - (m1+m2)*g*np.sin(u[0]) ) /( L1 *(m1+m2*s**2) )
    du[2] = u[3]   # d(theta 2)   
    du[3] = ((m1+m2)*(L1*u[1]**2*s - g*np.sin(u[2]) + g*np.sin(u[0])*c) + m2*L2*u[3]**2*s*c) / (L2 * (m1 + m2*s**2))
    
    return du
    
sol = odeint(Pen_dob, u0, t, args=(m1,m2,L1,L2,g))
u0 = sol[:,0]      
u1 = sol[:,1]   
u2 = sol[:,2]     
u3 = sol[:,3]   

# Cambio de coordenadas polares a cartesianas 

# Primer pendulo
x1 = L1*np.sin(u0);          
y1 = -L1*np.cos(u0);
# Segundo pendulo
x2 = x1 + L2*np.sin(u2);     
y2 = y1 - L2*np.cos(u2);


#Mapeo en el mapa cartesiano
ax = plt.subplot(3, 2, (1, 3))
ax.plot(x1,y1,'.',color = '#003ff5',label = 'Pendulo 1')    #Solucion de la primer ec dif
ax.plot(x2,y2,'-',color = '#f50000',label = 'Pendulo 2' )   #Solucion de la segunda ec dif
py.xlabel('x')
py.ylabel('y')


# Grafica Posicion tiempo
ax = plt.subplot(2, 2, 2)
ax.plot(t, u0, label=r"$\theta_1(t)$")
ax.plot(t, u2, label=r"$\theta_2(t)$")
plt.ylabel(r"$\theta$, [rad]")
plt.xlabel(r"$t$, [s]")
plt.xlim([0, np.max(t)])
plt.show
# Grafica Velocidad tiempo
ax = plt.subplot(2, 2, 4)
ax.plot(t, u1, label=r"$\omega_1(t)$")
ax.plot(t, u3, label=r"$\omega_2(t)$")
plt.ylabel(r"$\omega$, [rad/s]")
plt.xlabel(r"$t$, [s]")
plt.xlim([0, np.max(t)])
plt.show()