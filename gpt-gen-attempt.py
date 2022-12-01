import psutil

def main():
	# Get the PID of the process to attach to
	pid = int(input("Enter the PID of the process to attach to: "))

	# Attach to the process
	process = psutil.Process(pid)

	# Dump the virtual memory of the process
	memory_info = process.memory_info()
	print(memory_info)

	# Search for any http, https, and IP address regexes
	import re

	http_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
	ip_regex = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

	for memory_string in memory_info:
		http_matches = re.findall(http_regex, memory_string)
		print("HTTP matches:", http_matches)
		ip_matches = re.findall(ip_regex, memory_string)
		print("IP address matches:", ip_matches)

if __name__ == "__main__":
	main()