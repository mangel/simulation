class Orbit:
	previous = None
	def __init__(self, seed):
		self.seed = seed
		self.n = 0

	def f(self, x):
		result = None
		if (0 <= x and x < 0.5):
			result = 2*x
		elif (0.5 <= x and x < 1):
			result = 2*x - 1
		return result
	
	def step(self):
		if self.n == 0:
			self.previous = self.f(self.seed)
		else:
			self.previous = self.f(self.previous)
		result = self.previous
		self.n = self.n + 1
		return self.n, result
			
seed = 0.6
o = Orbit(seed)
MAX = 100

for i in range(0, MAX):
	step, value = o.step()
	print("Iteration: {}, value: {}".format(step, value))
