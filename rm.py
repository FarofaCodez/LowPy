import os
import sys
for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		os.remove(sys.argv[i])