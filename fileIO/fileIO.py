with open("file.txt") as f:
    for x in f:
        print(x,end="")

with open("out_file.txt", "w") as f:
    for i in range(10):
        f.write(f"Line{i + 1}\n")

print("==========================")

with open("out_file.txt") as f:
    for x in f:
        print(x,end="")

import os
if os.path.exists("out_file.txt"):
    os.remove("out_file.txt")
