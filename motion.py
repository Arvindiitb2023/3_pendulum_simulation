import numpy as np

class PendulamMotion:
    def __init__(self):
        self.omega = 10
        self.dt = 0.001
        self.L  = 1
    def rotation(self,state):
        theta1,theta2,theta3 = state

        theta1 = theta1 + 69*self.dt
        theta2 = theta2 + 169*self.dt
        theta3 = theta3 + 500*self.dt

        return [theta1,theta2,theta3]


