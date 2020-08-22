from datetime import datetime
import math

l_nm2 = 2
l_nm1 = 1

l_n = 0

n = 0
MAX = 70000
# hours * minutes * seconds
MAX_EXECUTION_IN_SECONDS = 1*1*3

begining_at = datetime.now()
iteration_begin_at = datetime.now()

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
		n = n + 1

		now = datetime.now()
		delta = now - begining_at

		if (n % 100000) == 0:
			print("Iteration {} reached. Iteration time(s): {}, acumulated time(s): {}.".format(n, (now - iteration_begin_at).total_seconds(), delta.total_seconds()))
			#print(l_n)
			iteration_begin_at = datetime.now()

		if delta.total_seconds() >= MAX_EXECUTION_IN_SECONDS:
			print("Last iteration reached at {}. Iteration time(s): {}, acumulated time(s): {}.".format(n, (now - iteration_begin_at).total_seconds(), delta.total_seconds()))
			break
except OverflowError as err:
	now = datetime.now()
	delta = now -begining_at
	print("Overflow error after {} seconds, on iteration {}".format(delta.total_seconds(),n))
	print("Previous two numbers")
	print(l_n)
	print(l_nm1)
