import matplotlib.pyplot as plt
import numpy as np
import random 
import math

class Terrain: 
	# Contructor
	def __init__(self, 
				startPoint = 0.0, 
				endPoint = 9.0, 
				segCount = 10,
				xlim = (0,9), 
				ylim = (0,1) 
				): 
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.segCount = segCount
		self.segLength = (self.endPoint - self.startPoint + 1)/segCount
		self.xlim = xlim
		self.ylim = ylim 
		self.pointList = []
		for i in range(self.segCount): 
			self.pointList += [random.uniform(self.ylim[0], self.ylim[1])]


	def drawTerrain(self): 
		fig = plt.figure()
		ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=self.xlim, ylim=(0,10))
		plt.plot(self.pointList)
		plt.show()

	def getYValue(self, x): 
		x1 = int(math.floor(x/self.segLength))
		x2 = x1 + 1
		if x2 >= self.xlim[1]: 
			return self.pointList[self.xlim[1]]
		y1 = self.pointList[x1]
		y2 = self.pointList[x2]
		m = (float)(y2-y1)/(x2-x1)
		return y1 + m*(x-x1)

	def getSlope(self, x): 
		x1 = int(math.floor(x/self.segLength))
		x2 = x1 + 1
		if x1 == self.xlim[1]: 
			y1 = self.pointList[x1-1]
			y2 = self.pointList[x1]
		else: 
			y1 = self.pointList[x1]
			y2 = self.pointList[x2]
		return (float)(y2-y1)/(x2-x1)

	def getPointList(self): 
		return self.pointList

	def setPointList(self, pointList): 
		self.pointList = pointList 
		self.segCount = len(pointList)
		

