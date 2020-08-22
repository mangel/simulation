import matplotlib.pyplot as plt

class Orbit:
	def __init__(self, seed):
		self.seed = seed
		self.n = 0
		self.previous = None
		self.X = []
		self.Y = []

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
		self.Y.append(self.previous)
		self.X.append(self.n)
		result = self.previous
		self.n = self.n + 1
		return self.n, result
			
MAX = 100
seeds = [0, 0.001, 0.25, 0.5, 0.999]
total_seeds = len(seeds)
Os=[]

#Initalization
format_str = "%d"
values = [0]
for seed in seeds:
	format_str = format_str + ",%f"
	Os.append(Orbit(seed))
	values.append(seed)

print(format_str % tuple(values))

for i in range(0, MAX):
	values = [i+1]
	for o in Os:
		n, result = o.step()
		values.append(result)
	print(format_str % tuple(values))

row_index = 0

fig, axes = plt.subplots(total_seeds,1)

for o in Os:
	axes[row_index].plot(o.X, o.Y)
	axes[row_index].set_title(r'Seed: ${}$'.format(o.seed))
	axes[row_index].set_ylabel(r'$F^n(x_n)$')
	row_index = row_index + 1
fig.subplots_adjust(hspace=1.5)
plt.show()
