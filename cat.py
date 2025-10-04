import sys
for i in range(len(sys.argv)):
	if i == 0:
		continue
	else:
		try:
			with open(sys.argv[i]) as file:
				print(file.read(), end="")
		except:
			print(f"Failed to open file {sys.argv[i]}")