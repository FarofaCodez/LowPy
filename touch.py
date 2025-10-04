import sys
for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		file = open(sys.argv[i], "w")
		file.close()