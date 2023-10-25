import subprocess
import re

#getting sha of last commit
repo_url = 'https://github.com/Di0Zavr/ItmoCloud_lab3'
process = subprocess.Popen(["git", "ls-remote", repo_url], stdout=subprocess.PIPE)
stdout, stderr = process.communicate()
sha = re.split(r'\t+', stdout.decode('ascii'))[0]

with open("output.txt", "w") as f:
	f.write(f"Hello, world!\nYour commit's sha is {sha}")
