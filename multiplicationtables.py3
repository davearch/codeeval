import math
import sys
for i in range(1,13):
	for j in range(1,13):
		rul = j * i
		sys.stdout.write((4 - int(math.log10(rul) + 1)) * ' ')
		sys.stdout.write(str(rul))
	if i != 12:
		print('\n')
