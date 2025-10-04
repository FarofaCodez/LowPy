import sys
for i in range(len(sys.argv)):
	if i == 0:
		continue
	if i != len(sys.argv):
		print(sys.argv[i], end=" ")
	else:
		print(sys.argv[i], end="\n")