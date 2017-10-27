###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

import numpy as np
import time

class Plane:
	def __init__(self, sleep_time, boundary, correction, **gauss_parameters):
		self.mu = gauss_parameters['mu']
		self.sigma = gauss_parameters['sigma']
		self.sleep_time = sleep_time
		self.correction = correction
	
		self.orientation = np.random.uniform(-boundary, boundary)

	def fly(self):
		while True:
			time.sleep(self.sleep_time)
			turbulation = np.random.normal(self.mu, self.sigma)
			self.orientation += turbulation
			self.orientation = self.orientation - self.correction if self.orientation > 0 else self.orientation + self.correction
			
			print(self)

	def __str__(self):
		return str(self.orientation)

if __name__ == "__main__":
	plane = Plane(sleep_time=0.2, boundary=30, correction=0.5, mu=0, sigma=1)
	print "Orientation at the beginning: %s" % (plane)
	plane.fly()



