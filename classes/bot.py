class Bot: 
	"""
	init_state is a 4 element tuple, representing (x, y, vx, vy)
    """
	def __init__(self, 
				init_state = (-3.2, -2.4, 0.5, 0.7)): 
		self.state = init_state
