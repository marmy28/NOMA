import os
hiddennomapath=os.path.join(os.path.expanduser('~'),'.noma/')
try:
	fin = open(hiddennomapath)
except(IOError):
	try:
		os.makedirs(hiddennomapath)
	except (OSError):
		mer = 0
