import os
import random

if not os.path.exists("file.txt"):
    with open("file.txt", "w") as f:
        f.write("")

for i in range(1, 365):
    for j in range(0, random.randint(1, 10)):
        d = str(i) + ' days ago'
        with open("file.txt", "a") as f:
            f.write(d + '\n')
        os.system("git add .")
        commit_command = f"git commit --date=\"{d}\" -m 'commit'"
        print(commit_command)  # Print the commit command for debugging
        os.system(commit_command)

os.system("git push origin main")
