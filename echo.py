import sys
for i in range(len(sys.argv)):
	if i != len(sys.argv):
		print(sys.argv[i], end=" ")
	else:
		print(sys.argv[i], end="\n")