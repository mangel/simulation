import matplotlib.pyplot as plt
from sympy import *

class Orbit:
	def __init__(self, seed):
		self.seed = seed
		self.n = 0
		self.previous = None
		self.X = []
		self.Y = []
		self.x = symbols('x')
		self.symbfn_1 = 2*self.x
		self.symbfn_2 = 2*(self.x)-1

	def f(self, x_in):
		result = None
		if (0 <= x_in and x_in < 0.5):
			result = self.symbfn_1.subs(self.x, x_in)
		elif (0.5 <= x_in and x_in < 1):
			result = self.symbfn_2.subs(self.x, x_in)
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
seed_1, seed_2, seed_3, seed_4, seed_5, seed_6 = symbols('seed_1 seed_2 seed_3 seed_4 seed_5 seed_6')
seed_1 = 0
seed_2 = Rational(1,1000)
seed_3 = Rational(1,4)
seed_4 = Rational(1,2)
seed_5 = Rational(999,1000)
seed_6 = Rational(1,9)

seeds = [seed_1, seed_2, seed_3, seed_4, seed_5]
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
