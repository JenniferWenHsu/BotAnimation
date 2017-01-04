class Bot: 
	def __init__(self, startPos = (0,0)): 
		self.currentPos = startPos

	def getPos(self): 
		return self.currentPos