"""
CONST_RED = 0
CONST_BLUE = 1
CONST_GREEN = 2
CONST_WHITE = 3
CONST_YELLOW = 4
CONST_ORANGE = 5
"""	

class Faccia:
	def __init__(self, color):
		f_vicine = [[1], [1], [1], [1], [2], [3]]
		
		self.color = color
		self.facce_vicine = f_vicine[color]
		self.faccia = [[0]*3]*3
	
	def set_face(self, matrix):
		self.faccia = matrix
	
	def rotate(self, direction):
		pass
	
	def get_side(self, side):
		pass
	
	def set_side(self, side):
		pass
	
	def __str__(self):
		_str = ''
		for i in self.faccia:
			for t in i:
				_str += str(t)+' '
			_str += '\n'
		return _str	
		
class Cubo:
	def __init__(self):
		self.cubo = []
		for i in range(6):
			self.cubo += [Faccia(i)]
	
	def move(self, code):
		pass
	
	def complete_block(self, _id):
		pass
	
	
cubo = Cubo()
print(cubo)
