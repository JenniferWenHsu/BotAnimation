class Bot: 
	"""
	init_state is a 4 element tuple, representing (x, y, vx, vy)
    """
	def __init__(self, 
				init_state = [1, 5, 0.5, 0]): 
		self.state = init_state

	def getState(self): 
		return self.state