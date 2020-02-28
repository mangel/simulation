def decompose(number):
  n = 1
  digits = []
  while number != 0:
    digit = number % 10**n
    digits.append(int(digit/10**(n-1)))
    number = number - digit
    n = n + 1
  return digits

def compose(digits):
  result = 0
  for i, d in enumerate(digits):
    result = result + d*(10**i)
  return result

def nMSD(number,n=1):
  float_part = number % 1
  integer_part = number
  if float_part > 0:
    integer_part = int (number - float_part)
  return decompose(integer_part)[-n]

def decrease_nonzero_digits(number):
  digits = decompose(number)
  for i,d in enumerate(digits):
    if d !=0:
      d = d -1
    digits[i] = d
  return compose(digits)

def print_step(x,y):
  print("X: {}, Y: {}".format(x,y))

# X must be 10 digit number
X = 1234567890
#K1 Choose random number of iterations
Y = X/(10**9)
print_step(X,Y)

n = 0

while n <= Y + 1:
  #K2 Choose random step
  Z = (X/10**8) % 10
  next_step = 3 + Z

  #K3 Ensure >= 5*10**9
  if next_step == 3:
    if X < 5000000000:
      X = X + 5000000000
  #K4 Middle square
  elif next_step == 4:
    X = ((X**2) / (10**5)) % (10**10)
  #K(5,8) Multiply
  elif next_step == 5 or next_step == 8:
    X = (1001001001*X) % (10**10)
  #K6 Pseudo-complement
  elif next_step == 6:
    if X < 100000000:
      X = X + 9814055677
    else:
      X = (10**10) - X
  #K7 Interchange halves
  elif next_step == 7:
    X = (10**5) * (X % (10**5)) + (X/(10**5))
  #K9 Decrease digits
  elif next_step == 9:
    X = decrease_nonzero_digits(X)
  #K10 99999 modify
  elif next_step == 10:
    if X < 10**5:
      X = X**2 + 99999
    else:
      X = X - 99999
  #K11 Normalize
  elif next_step == 11:
    if X < 10**9:
      X = 10*X
      X = 10*X
  #K12 Modified middle square
  elif next_step == 12:
    X = (X*(X-1)/(10**5)) % (10**10)
  #K13 Repeat
  elif next_step == 13:
    if Y > 0:
      Y = Y -1
      continue
    elif Y == 0:
      break

print(X)
