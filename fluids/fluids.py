from vectors import Vector 
from particles import Particle
import random


class Fluid:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.particles = []
        self.velocity = []


    def add_particles(self, particles):
        particles_qnt = len(particles[0])
        for i in range(particles_qnt):

            x,y,z = particles[0][i], particles[1][i], particles[2][i]
            position = (x,y,z)
            velocity = (random.randint(-1, 1),random.randint(-1, 1),random.randint(-1, 1))
            particle = Particle(position,velocity)
            self.particles.append(particle)
            self.matrix.data[x,y,z] = 1
            
    def flow(self):
        for particle in self.particles:
            velocity = particle.get_velocity()
            vector = velocity.get_vector()
            vel_vector = vector.get_position()

            position = particle.get_position()
            
            newx = position[0]+vel_vector[0]
            if self.matrix.data.shape[0] <= newx or newx < 0:
                particle.change_velocity((-vel_vector[0], vel_vector[1], vel_vector[2]))
                newx = position[0]
                
            newy = position[1]+vel_vector[1]
            if self.matrix.data.shape[1] <= newy or newy < 0:
                particle.change_velocity((vel_vector[0], -vel_vector[1], vel_vector[2]))
                newy = position[1]

            newz = position[2]+vel_vector[2]
            if self.matrix.data.shape[2] <= newz or newz < 0:
                particle.change_velocity((vel_vector[0], vel_vector[1], -vel_vector[2]))
                newz = position[2]
            
            self.matrix.data[position[0], position[1], position[2]] = 0
            self.matrix.data[newx, newy, newz] = 1
            
            newpos = (newx, newy,newz)
            particle.set_position(newpos)
            
            #print(particle.get_position())

