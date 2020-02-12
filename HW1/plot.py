import matplotlib.pyplot as plt
from datetime import datetime
import math

x = []
y = []

index = 1
l_nm2 = 2
l_nm1 = 1

l_n = 0

n = 0
MAX = 70000

begining_at = datetime.now()
iteration_begin_at = datetime.now()
timed_report = datetime.now()

# Set this variable to true to run indefinetly.
BYPASS = False
# hours * minutes * seconds. Set this variable to change the maximum execution time.
MAX_EXECUTION_IN_SECONDS = 1*1*0.05
# Status report iterations
STATUS = 1

print("MAX_EXECUTION_IN_SECONDS: {}".format(MAX_EXECUTION_IN_SECONDS))
try:
	while True:
		if n == 0:
			l_n = 2
		elif n == 1:
			l_nm1 = l_n
			l_n = 1
		else:
			l_nm2 = l_nm1
			l_nm1 = l_n
			l_n = l_nm1 + l_nm2

		x.append(n)
		y.append(l_n)

		n = n + 1

		now = datetime.now()
		delta = now - begining_at


		if (n % STATUS) == 0:
			print("Iteration {} reached. Iteration time(s): {}, acumulated time(s): {}.".format(n, (now - iteration_begin_at).total_seconds(), delta.total_seconds()))
			print("#{}|{}".format(n,l_n))
			iteration_begin_at = datetime.now()

		if delta.total_seconds() >= MAX_EXECUTION_IN_SECONDS and not BYPASS:
			print("Last iteration reached at {}. Iteration time(s): {}, acumulated time(s): {}.".format(n, (now - iteration_begin_at).total_seconds(), delta.total_seconds()))
			print("Last Ln: {}".format(l_n))
			break
except OverflowError as err:
	now = datetime.now()
	delta = now -begining_at
	print("Overflow error after {} seconds, on iteration {}".format(delta.total_seconds(),n))
	print("Previous two numbers")
	print(l_n)
	print(l_nm1)

plt.plot(x,y, label='L_n')
plt.xlabel('iteration')
plt.ylabel('Lucas Number (L_n))')
plt.title('Iteration vs Lucas Number')
plt.legend()
plt.show()
