from vector import *
import matplotlib.pyplot as plt
import numpy as np

def grav_force(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 6 # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    
    return force_vec

class star:
    #any class attributes?
    #add luminosity? color?
    def __init__(self, radius: float, mass: float, 
                 pos = vector(0,0,0), momentum = vector(0,0,0)):
        #data validations
        assert radius >=0, 'mf'
        assert mass >=0, 'mf'
        
        
        #assign to self object
        self.pos = pos
        self.radius = radius
        self.mass = mass
        self.momentum = momentum
    
    def velocity(self):
        return self.momentum/self.mass
    
    def orbit_plot(self):
        pass
    
star1 = star(6, 20, pos=vector(0,0,0), momentum=vector(30,30,8))
star2 = star(3, 20, pos=vector(0,6,0), momentum=vector(-30,-30,-8))
print(star1.velocity())        
print(star2.velocity())

star1.orbit = [[],[]]
star2.orbit = [[],[]]

dt = 0.0001
t = 0
while (t<3):
    # Calculate forces.
    star1.force = grav_force(star1,star2)
    star2.force = grav_force(star2,star1)
    # Update momenta.
    star1.momentum = star1.momentum + star1.force*dt
    star1.orbit[0].append(star1.momentum)
    star2.momentum = star2.momentum + star2.force*dt
    star2.orbit[0].append(star2.momentum)
    # Update positions.
    star1.pos = star1.pos + star1.momentum/star1.mass*dt
    star1.orbit[1].append(star1.pos)
    star2.pos = star2.pos + star2.momentum/star2.mass*dt
    star2.orbit[1].append(star2.pos)
    t = t + dt
    
    


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.scatter([star1.orbit[1][i].x for i in range(len(star1.orbit[1]))] ,
        [star1.orbit[1][i].y for i in range(len(star1.orbit[1]))], 
        [star1.orbit[1][i].z for i in range(len(star1.orbit[1]))], s=0.05)
ax.scatter([star2.orbit[1][i].x for i in range(len(star2.orbit[1]))] ,
        [star2.orbit[1][i].y for i in range(len(star2.orbit[1]))], 
        [star2.orbit[1][i].z for i in range(len(star2.orbit[1]))], s=0.05)

plt.show()