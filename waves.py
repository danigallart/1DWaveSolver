import numpy as np
import matplotlib.pyplot as plt

#define the 1D grid for the wave function
L = 5
x_total_points = 130
dx = 5./x_total_points
x_grid = np.linspace(0,L,x_total_points)

#define the time grid
t_total = 5
t_total_points = 1000 
dt = t_total/t_total_points
t_grid = np.linspace(0,t_total,t_total_points)

#define the wave function and the initial and boundary conditions
u = np.zeros((x_total_points,t_total_points))
u[0,:] = 0.
u[L,:] = 0.
c = 4.
alpha = 0.

for i in range(1,len(u)-1):
    u[i,0] = 8.*x_grid[i] * (L-x_grid[i])**2/L**3

#compute with the boundary and initial conditions the first time step, i.e., u[i,1]
for i in range(1,len(x_grid)-1):
    u[i,1] = 1./2.*dt**2*c**2/dx**2*(u[i-1,0]-2.*u[i,0] + u[i+1,0]) + u[i,0] + dt*alpha

#compute now the rest of the time points
for j in range(1,len(t_grid)-1):
    for i in range(1,len(x_grid)-1):
        u[i,j+1] = dt**2*c**2/dx**2*(u[i-1,j] - 2.*u[i,j] + u[i+1,j]) + 2*u[i,j] - u[i,j-1]

a = 500
fig = plt.figure(figsize=(15,6))
for i in range(t_total_points):
    if i % 5 == 0:
        plt.clf()
        plt.xlim()
        plt.ylim(-1.5,1.5)
        plt.title('Time:' + '{:.2f}s'.format(dt*i))
        plt.plot(x_grid,u[:,i])
        plt.pause(0.001)
#print('time:', a*dt)
plt.show()

#animating the evolution of the wave
#import matplotlib.animation as animation
#ims=[]
#fig = plt.figure(figsize=(15,4))
#for i in range(t_total_points):
#    im = plt.plot(x_grid,u[:,i],animated=True)
#    ims.append([im])
#ani = animation.ArtistAnimation(fig, ims)
#ani.save('file')
