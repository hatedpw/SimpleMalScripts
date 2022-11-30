# attach to current running process via PID and read the memory then pull strings from the memory and search for http, https, and ip adress regex

import sys
import os
import re
import psutil

def mempull():
	if len(sys.argv) != 2:
		print("Usage: python3 MemIPPull.py <PID>")
		sys.exit(1)
	else:
		pid = sys.argv[1]
		if psutil.pid_exists(int(pid)):
			try:
				process = psutil.Process(int(pid))
				mem = process.memory_maps()
				for m in mem:
					#writes to a file
					with open(pid + "mem.txt", "a") as f:
						f.write(str(m))
						f.write("\n")
			except:
				print("Error reading file")

def main():
	mempull()
	#searches for http and https
	with open("mem.txt", "r") as f:
		for line in f:
			if "http" in line:
				print(line)
			elif "https" in line:
				print(line)
			elif re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line):
				print(line)
			elif 
			#search for base64 encoded strings
			elif re.search(r"[A-Za-z0-9+/]{4}={0,3}", line):
				print(line)
			else:
				continue

if __name__ == "__main__":
	main()
