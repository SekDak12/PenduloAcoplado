# Codigo Pendulo Simple Runge-Kutta
# Datos del pendulo 1

import numpy as np 
import matplotlib.pyplot as plt 

g=9.81 #Gravedad del planeta
I=2 #Longitud de la cuerda
h=0.025 #Tamaño de paso 
t= np.arange(0,10,h) #arreglo tiempo (Tiempo inicial, Tiempo final, Paso)
theta_0=1 #Angulo inicial
m=10 #masa del penndulo
n= len(t)
y=np.zeros(n)
v=np.zeros(n)

def PenSim(theta):
    PenSim = -(g/I)*np.sin(theta)
    return PenSim

y[0] = np.radians(theta_0) 
v[0] = np.radians(0)

for i in range(0, n-1):            #Metodo de Runge-Kutta de 4to orden
    k1y = h*v[i]
    k1v = h*PenSim(y[i])
    k2y = h*(v[i]+0.5*k1v)
    k2v = h*PenSim(y[i]+0.5*k1y)
    k3y = h*(v[i]+0.5*k2v)
    k3v = h*PenSim(y[i]+0.5*k2y)
    k4y = h*(v[i]+k3v)
    k4v = h*PenSim(y[i]+k3y)
    # Nuevos valores de Y y V
    y[i+1] = y[i] + (k1y + 2 * k2y + 2 * k3y + k4y) / 6.0 
    v[i+1] = v[i] + (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0

def Up(u):          #Energia Potencial del pendulo simple
    return m*g*I*(1 - np.cos(u))

def K(u):          #Energia Cinetica del pendulo simple
    return 0.5*m*I**2*np.array(u)**2

plt.plot(np.sin(y), -I*np.cos(y),'.', color = '#f50000')
plt.title('Mapeo del pendulo Simple:')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.show()


plt.title("Grafica Angulo-Tiempo ")
plt.plot(t, y, "m")
plt.xlabel(r"$t$, [s]")
plt.ylabel(r"$\theta(t)$, [rad]")
plt.show()


plt.title(r"Energia Mecanica ")
plt.plot(t, Up(y), label=r"Energia Potenical")
plt.plot(t, K(v), label=r"Energia Cinetica")
plt.xlabel(r"$t$, [s]")
plt.ylabel(r"$E$, [J]")
plt.legend(loc=1)
plt.show()