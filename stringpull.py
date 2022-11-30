#pull char from a binary file param given via cli and return strings into a file name after the file name.strings.txt

import sys
import os
import re

def pullstring():
	if len(sys.argv) != 2:
		print("Usage: python3 stringpull.py <file>")
		sys.exit(1)
	else:
		file = sys.argv[1]
		if os.path.exists(file):
			try:
				with open(file, 'rb') as f:
					data = f.read()
					strings = re.findall(b'[A-Za-z0-9]{4,}', data)
					with open(file + ".strings.txt", 'w') as f:
						for string in strings:
							f.write(string.decode('utf-8') + "\n")
			except:
				print("Error reading file")

# from the newly made file remove any line with less than 7 chars
def remove():
	with open(sys.argv[1] + ".strings.txt", "r") as f:
		lines = f.readlines()
	with open(sys.argv[1] + ".strings.txt", "w") as f:
		for line in lines:
			if len(line) > 7:
				f.write(line)

# extract any line with http or https, or an ip address regex and print to terminal
def extract():
	with open(sys.argv[1] + ".strings.txt", "r") as f:
		lines = f.readlines()
	for line in lines:
		if "http" in line:
			print(line)
		elif "https" in line:
			print(line)
		elif re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line):
			print(line)
		elif re.match(r"[A-Za-z0-9+/]{4}={0,3}", line):
			print(line)

if __name__ == "__main__":
	pullstring()
	remove()
	extract()
