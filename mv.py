import sys
import os
toMove = []
for i in range(len(sys.argv)):
	if i == 0:
		continue
	if i != len(sys.argv):
		toMove.append(sys.argv[i])
	else:
		target = sys.argv[i]

for item in toMove:
	os.rename(item, target)