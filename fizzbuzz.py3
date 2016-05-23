import sys

def fizzbuzz(z,y,x):
	text = []
	for i in range(1, x+1):
		f = (i % z)
		b = (i % y)
		if f == b == 0:
			text.append('FB')
		elif f == 0:
			text.append('F')
		elif b == 0:
			text.append('B')
		else:
			text.append(str(i))
	print(" ".join(text)),

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		results = list(map(int, test.split()))
		fizzbuzz(results[0],results[1],results[2])
