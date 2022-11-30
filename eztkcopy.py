# read current file directory and return the file name, md5,sha25 and file size. does not include this python file.
import os
import hashlib
import sys


def hashfile(path, blocksize = 65536):
	try:
		afile = open(path, 'rb')
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
	except:
		return "failed to extract md5"

def hashfile2(path, blocksize = 65536):
	afile = open(path, 'rb')
	try:
		hasher = hashlib.sha256()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
		afile.close()
		return hasher.hexdigest()
	except:
		return "failed to extract sha256"


def GetCurrentDirectory():
	return os.getcwd()
def main():
	GetCurrentDirectory()
	for root, dirs, files in os.walk(GetCurrentDirectory()):
		for file in files:
			if file == "eztikcopy.py":
				continue
			path = (file)
			print("Filename:", path)
			print("MD5:", hashfile(path))
			print("SHA256:", hashfile2(path))
			print("File size:", os.path.getsize(path), "bytes \n")


if __name__ == "__main__":
	main()
